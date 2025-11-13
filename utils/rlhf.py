"""
TRL Documentation reference:
    Reward Modelling and how to write reward functions documentation: https://huggingface.co/docs/trl/main/en/reward_trainer
    GRPO Trainer and Config : https://huggingface.co/docs/trl/main/en/grpo_trainer 

"""


import unsloth
from unsloth import FastLanguageModel
from trl import GRPOConfig, GRPOTrainer, RewardTrainer, RewardConfig
import torch
import random
import json
import datasets
from datasets import load_dataset
from typing import List, Dict
from collections import defaultdict
import re
from tqdm import tqdm
from string import Template
from vllm import SamplingParams
import evaluate

from utils.generate import OClientModel, OModelConfig, HCLientModel, HModelConfig
from peft import LoraConfig, TaskType, get_peft_model, PeftModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer, BitsAndBytesConfig



class RLHFEntityPRL:
    def __init__(self, ollama_model : OClientModel,  
                 model_name : str,
                 max_extractive_ans_len : int = 8, 
                 max_seq_len : int = 4196, 
                 lora_rank : int = 16):
        
        """
        Args:
            ollama_model : verification model which verifies the prompt
            model_name : policy model name
            max_extractive_ans_len : threshold for factoid answer
            max_seq_len : model specific max length
            lora_rank : lora rank for adapter


            Important note: try to increase gpu_memory_utlization during inference. 
        """
        
        self.ollama_model = ollama_model
        self.ollama_config = OModelConfig(temperature=0.7, top_p=0.9, seed = 42)
        self.ollama_responses = None

        self.model_name = model_name
        self.extractive_answer_len = max_extractive_ans_len
        self.max_seq_len = max_seq_len
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_name=model_name,
            load_in_4bit=True,
            max_lora_rank=lora_rank,
            gpu_memory_utilization=0.5,
            fast_inference = True
        )

        self.model = FastLanguageModel.get_peft_model(
            self.model,
            r = lora_rank,
            target_modules = [
                "q_proj", "k_proj", "v_proj", "o_proj",
                "gate_proj", "up_proj", "down_proj",
            ],
            lora_alpha=lora_rank*2,
            use_gradient_checkpointing="unsloth",
            random_state=3407
        )
    
    def hard_parse_ollama(self, generated_text : str):
        """
            Parser to evaluate the answering format which the new prompt must contain
        """
        results = []
        pattern = re.compile(
            r"Answer Sample:\s*(?P<ans>.*?)\s*"  
            r"Explanation:\s*(?P<explanation>.*?)(?=\nAnswer Sample:|\Z)", 
            re.IGNORECASE | re.DOTALL
        )

        for match in pattern.finditer(generated_text):
            answer = match.group("ans").strip()
            explanation = match.group("explanation").strip()
            answer = answer.replace("*","").strip()
            answer = answer.replace("\n","").strip()

            explanation = explanation.replace("*","").strip()
            explanation = explanation.replace("\n","").strip()
            results.append((answer, explanation))

        return results
    
    def soft_parse_ollama(self, generated_text: str):
        """
            Parser to evaluate the answering format which the new prompt must contain
        """
        results = []
        # This pattern handles optional asterisks around the labels.
        pattern = re.compile(
            r"\*?Answer Sample\*?:\s*(?P<ans>.*?)\s*"
            r"\*?Explanation\*?:\s*(?P<explanation>.*?)(?=\n\*?Answer Sample\*?:|\Z)",
            re.IGNORECASE | re.DOTALL
        )

        for match in pattern.finditer(generated_text):
            answer = match.group("ans").strip()
            explanation = match.group("explanation").strip()

            answer = answer.replace("*","").strip()
            answer = answer.replace("\n","").strip()

            explanation = explanation.replace("*","").strip()
            explanation = explanation.replace("\n","").strip()
            results.append((answer, explanation))

        return results

    def extract_xml_answer(self, text : str):
        answer = text.split("<output>")[-1]
        answer = answer.split("</output>")[0]
        return answer.strip()

    def special_token_reward(self, completions, **kwargs):
        """
            Reward Function: 
                To check the output of the policy model to see if it has
                <think>, </think>, <output> and </output>
        """
        completions = [completion[0]["content"] for completion in completions]
        rewards = []
        for text in completions:
            reward = 0
            if "<think>" in text:
                reward += 0.25
            else:
                reward -= 1.0
            
            if "</think>" in text:
                reward += 0.25
            else:
                reward -= 1.0

            if "<output>" in text:
                reward += 0.25
            else:
                reward -= 1.0

            if "</output>" in text:
                reward += 0.25
            else:
                reward -= 1.0

            rewards.append(reward)
        return rewards

    def soft_structure_reward(self, completions, **kwargs):
        completions = [completion[0]["content"] for completion in completions]
        soft_pattern = r"<think>.*?</think>\s*<output>.*?</output>"

        rewards = []
        for text in completions:
            reward = 0.0
            soft_match = re.match(soft_pattern, text)
            if soft_match:
                reward += 1.0

            rewards.append(reward)

        return rewards
    
    def exact_structure_reward(self, completions, **kwargs):
        """
        Reward Function:
            The output should be of the format,
            <think>
            blah, blah and blah
            </think>
            <output>
            blah blah and blah
            </output>
        """
        completions = [completion[0]["content"] for completion in completions]
        reasoning_start = r"<think>"
        reasoning_end = r"</think>"
        solution_start = r"<output>"
        solution_end = r"</output>"

        # The regex to match the format
        # It captures the content inside <output>...</output>
        match_format = re.compile(
            rf"^[\s]*"  # Optional leading whitespace from the start of the string/line
            rf"{re.escape(reasoning_start)}\n.*?\n{re.escape(reasoning_end)}[\s]*"  # Non-greedy match for <think> block with newlines, and optional whitespace after </think>
            rf"{re.escape(solution_start)}\n(.+?)\n{re.escape(solution_end)}[\s]*"  # Non-greedy capture of <output> content, with newlines, and optional whitespace after </output>
            rf"$",  # End of the string/line
            flags=re.MULTILINE | re.DOTALL
        )

        # Test the regex
        rewards = []
        for text in completions:
            reward = 0.0
            match = match_format.search(text)
            if match:
                reward += 1.0

            rewards.append(reward)

        return rewards
    
    def format_reward(self, completions, context, **kwargs):
        """
        Reward Function:
            The prompt when tested on another model should have the answer format,
            Answer: <answer string>
            Explantion: <explanation string>

            Answer: <answer string>
            Explanation: <explnation string>
        """
        # print(f"Completions format reward gen = {completions}", flush = True)
        # print(f"Context = {context}", flush = True)
        # print(f"Completions = {completions}", flush = True)
        completions = [f"Instruction:{self.extract_xml_answer(completion[0]["content"])}\nContext:{context_}" for context_, completion in zip(context,completions)]
        
        responses = [self.ollama_model(completion, **self.ollama_config.__dict__).response for completion in completions]
        # print(f"Ollama responses = {responses}", flush = True)
        self.ollama_responses = [response for response in responses]
        # parsed_responses = [self.hard_parse_ollama(text) for text in responses]
        parsed_responses = [self.soft_parse_ollama(text) for text in responses]

        # print(f"Hard Parsed Rewards = {parsed_responses}", flush = True)
        # print(f"Soft Rewards Responses = {parsed_responses}", flush = True)

        rewards = []
        for response in parsed_responses:
            if len(response) == 0:
                rewards.append(0.0)
            else:
                rewards.append(2.0)

        return rewards
    
    def factoid_answer_reward(self, completions : List[str], context : List[str], **kwargs):
        """
        Reward Functions:
            Because we are looking for factoid spans in the context, just verify that the answer of short length
        """
        completions = [f"Instruction:{self.extract_xml_answer(completion[0]["content"])}\nContext:{context_}" for context_, completion in zip(context,completions)]
        if self.ollama_responses is not None:
            responses = [response for response in self.ollama_responses]
        else:
            responses = [self.ollama_model(completion, **self.ollama_config.__dict__).response for completion in completions]

        parsed_responses = [self.soft_parse_ollama(text) for text in responses]
        rewards = []
        for response in parsed_responses:
            sample_reward = 0
            for resp_ in response:
                if len(resp_[0].split()) <= self.extractive_answer_len:
                    sample_reward += 1.0

            if len(response) > 0:
                rewards.append(sample_reward/len(response))
            else:
                rewards.append(0.0)

        return rewards
    

    def span_presence_reward(self, completions : List[List[Dict[str, str]]], context : List[str], **kwargs):
        """
        Reward Function:
            When the prompt is tested on some context and applied on some other model, the answers must be present in the context.
        """
        completions = [f"Instruction:{self.extract_xml_answer(completion[0]["content"])}\nContext:{context_}" for context_, completion in zip(context,completions)]
        if self.ollama_responses is not None:
            responses = [response for response in self.ollama_responses]
        else:
            responses = [self.ollama_model(completion, **self.ollama_config.__dict__).response for completion in completions]

        parsed_responses = [self.soft_parse_ollama(text) for text in responses]
        rewards = []
        for response, context_ in zip(parsed_responses, context):
            presence_reward = 0.0
            all_responses = [ans[0] for ans in response]

            for resp_ in all_responses:
                if resp_ in context_:
                    presence_reward += 1.0
                else:
                    presence_reward -= 0.5

            if len(response) > 0:
                presence_reward = presence_reward / len(response)
            else:
                presence_reward = 0.0

            rewards.append(presence_reward)

        return rewards


    def correctness_reward_func(self, completions : List[str], answer : List[str], context : str, **kwargs):
        """
        Reward Functions:
            When the prompt is tested on some context and applied on some other model, the answers must be compared whatever answers are present in the datasets.
        """
        # print(f"Completions format reward gen = {completions}", flush = True)
        # print(f"Context = {context}", flush = True)
        completions = [f"Instruction:{self.extract_xml_answer(completion[0]["content"])}\nContext:{context_}" for context_, completion in zip(context,completions)]
        if self.ollama_responses is not None:
            responses = [response for response in self.ollama_responses]
        else:
            responses = [self.ollama_model(completion, **self.ollama_config.__dict__).response for completion in completions]

        parsed_responses = [self.soft_parse_ollama(text) for text in responses]
        rewards = []
        for response, answer_ in zip(parsed_responses, answer):
            coverage_ = 0.0
            all_responses = [ans[0] for ans in response]
            for ans in answer_:
                if ans in all_responses:
                    coverage_ += 3.0
                else:
                    coverage_ -= 0.5

            if len(response) > 0:
                coverage_ /= len(answer_)
            else:
                coverage_ = 0.0
            rewards.append(coverage_)

        self.ollama_responses = None
        
        return rewards
    
    def prepare_dataset(self, 
                        data_name : str = "rajpurkar/squad", 
                        num_samples : int = 3000, 
                        disable_tqdm : bool = False):
        
        """
            system_prompt : Define how the response of the policy model should look like
            user_prompt : Base task
        """

        samples = datasets.load_dataset(data_name)["train"]
        augmented_samples = defaultdict(list)
        
        system_prompt = """A conversation between User and Assistant. The user gives a task, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user
with the output. The reasoning process must be enclosed within <think> </think> tags and the output must be enclosed within <output> </output> tags, i.e., the format should be,
<think>
reasoning process here.
</think>
<output>
output here 
</output>"""
        
        user_prompt = """Your task is to refine a base prompt for another model that performs answer extraction from a context provided externally by the user. Improve the base prompt to enhance the model's performance. You must ensure that the instruction must include output format for the another model.
Base prompt-You are a powerful language model designed to extract all possible short spans from a given context that could serve as answers to some potential questions.
Each span must include:
- "Answer Sample": the exact substring from the context.
- "Explanation" : what makes the text span a good answer span.

Your output format should follow the following format.
                          
Answer Sample: <answer sample>
Explanation: <explanation string>

Answer Sample: <answer sample>
Explanation: <explanation string>

Only output your answer according to the above format and nothing else.

Your Prompt-"""

        context_qa_dict = defaultdict(list)

        for idx in tqdm(range(0, num_samples), disable=disable_tqdm):
            context = samples["context"][idx]
            answers = samples["answers"][idx]["text"]
            answers = list(set(answers))

            context_qa_dict[context].extend(answers)

        for context, answers in tqdm(context_qa_dict.items(), disable = disable_tqdm):
            augmented_samples["context"].append(context)
            answers = list(set(answers))
            augmented_samples["answer"].append(answers)
            augmented_samples["system_prompt"].append(system_prompt)
            augmented_samples["user_prompt"].append(user_prompt)
            augmented_samples["prompt"].append([
                {"role" : "system", "content" : system_prompt},
                {"role" : "user", "content" : user_prompt}
            ])


        augmented_samples = datasets.Dataset.from_dict(augmented_samples)
        return augmented_samples
    

    def train(self, saved_model_name : str,
                  dataset : datasets.Dataset, 
                  output_dir : str = "outputs", 
                  max_steps : int = 1, 
                  max_prompt_length : int = 256):

        vllm_sampling_params = SamplingParams(
            min_p = 0.1,
            top_p = 1.0,
            top_k = -1,
            seed = 3407,
            stop = [self.tokenizer.eos_token],
            include_stop_str_in_output = True,
        )

        training_args = GRPOConfig(
            vllm_sampling_params = vllm_sampling_params,
            temperature = 1.0,
            learning_rate = 5e-6,
            weight_decay = 0.1,
            warmup_ratio = 0.1,
            lr_scheduler_type = "linear",
            optim = "adamw_8bit",
            logging_steps = 1,
            per_device_train_batch_size = 2,
            gradient_accumulation_steps = 1, # Increase to 4 for smoother training
            num_generations = 2, # Decrease if out of memory
            max_prompt_length = max_prompt_length,
            max_completion_length = self.max_seq_len - max_prompt_length,
            # num_train_epochs = 1, # Set to 1 for a full training run
            max_steps = max_steps,
            save_steps = 250,
            max_grad_norm = 1.0,
            report_to = "none", # Can use Weights & Biases
            output_dir = output_dir
        )
        trainer = GRPOTrainer(
            model = self.model,
            processing_class = self.tokenizer,
            reward_funcs = [
                self.special_token_reward,
                self.exact_structure_reward,
                self.format_reward,
                self.factoid_answer_reward,
                self.span_presence_reward,
                self.correctness_reward_func
            ],
            args = training_args,
            train_dataset = dataset,
        )
        
        trainer.train()
        self.model.save_lora(saved_model_name)

    def generate_inference(self,  
                           model_path : str,
                           num_sequences : int = 10,
                           temperature : float = 0.7,
                           max_seq_length : int = 4196):

        system_prompt = """A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user
with the output. The reasoning process must be enclosed within <think> </think> tags and the output must be enclosed within <output> </output> tags, i.e., the format should be,
<think>
reasoning process here.
</think>
<output>
output here 
</output>"""
        
        user_prompt = """Your task is to refine a base prompt for another model that performs answer extraction from a context. Improve the base prompt to enhance the model's performance. You must ensure that the instruction must include output format for the another model.
Base prompt-You are a powerful language model designed to extract all possible short spans from a given context that could serve as answers to some potential questions.
Each span must include:
- "Answer Sample": the exact substring from the context.
- "Explanation" : what makes the text span a good answer span.

Your output format should follow the following format.
                          
Answer Sample: <answer sample>
Explanation: <explanation string>

Answer Sample: <answer sample>
Explanation: <explanation string>

Only output your answer according to the above format and nothing else.

Your Prompt-"""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt = True, # Must add for generation
            tokenize = False,
        )

        sampling_params = SamplingParams(
            temperature = temperature,
            top_p = 0.95,
            max_tokens = max_seq_length,
        )

        sequences = []
        for _ in tqdm(range(num_sequences)):
            output = self.model.fast_generate(
                        text,
                        sampling_params = sampling_params,
                        lora_request = self.model.load_lora(model_path)
                    )[0].outputs[0].text

            # print(f"Outputs = {output}")
            # print(f"\n\n")

            sequences.append(output)

        return sequences

    
    def best_prompt_selections(self, sequences : List[str], test_context : str, topk : int = 10):
        assert self.ollama_model is not None, "ollama model cannot be None"

        completions = [[{"content": sequence }] for sequence in sequences]

        special_token_reward = self.special_token_reward(completions=completions)
        exact_structure_reward = self.exact_structure_reward(completions = completions)
        format_reward = self.format_reward(completions=completions, context = test_context)
        factoid_reward = self.factoid_answer_reward(completions=completions, context = test_context)

        net_reward = [sp_ + ex_ + form_ + fact_ for sp_, ex_, form_, fact_ in zip(special_token_reward, exact_structure_reward, format_reward, factoid_reward)]
        
        sequences = [(sequence, reward_) for sequence, reward_ in zip(sequences, net_reward)]
        sequences = sorted(sequences, key = lambda x : x[1], reverse = True)

        return sequences[:topk]



