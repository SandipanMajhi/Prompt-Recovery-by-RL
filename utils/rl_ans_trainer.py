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
from utils.rewards import RewardFuncs
from utils.generate import OClientModel, OModelConfig, HCLientModel, HModelConfig
from transformers import set_seed


class RLEntityPRL:
    def __init__(self,
                 policy_model_name : str,
                 max_seq_len : int = 8192,
                 lora_rank : int = 64,
                 is_inference : bool =  False,
                 lora_adapter_name : str = None,
                 use_vllm : bool = True
                 ):
        """
            use_vllm : For fast inference
            policy_model_name: Base model name
            is_inference: No Training if True
        """
        
        self.policy_model_name = policy_model_name
        self.max_seq_len = max_seq_len
        self.lora_rank = lora_rank
        self.use_vllm = use_vllm

        if not is_inference:

            self.model, self.tokenizer = FastLanguageModel.from_pretrained(
                model_name=policy_model_name,
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

        else:
            
            if not use_vllm:

                self.model, self.tokenizer = FastLanguageModel.from_pretrained(
                    model_name=policy_model_name,
                    load_in_4bit=True,
                    max_seq_length=max_seq_len,
                    dtype = None,
                    max_lora_rank=lora_rank
                )
            
            else:

                self.model, self.tokenizer = FastLanguageModel.from_pretrained(
                    model_name=policy_model_name,
                    load_in_4bit=True,
                    max_seq_length=max_seq_len,
                    dtype = None,
                    max_lora_rank=lora_rank,
                    fast_inference=True,
                    gpu_memory_utilization=0.5
                )


            self.model.load_adapter(lora_adapter_name)
            FastLanguageModel.for_inference(self.model)


    def train(self,
                  reward_functions, 
                  saved_model_name : str,
                  dataset : datasets.Dataset, 
                  output_dir : str = "outputs", 
                  max_steps : int = 1, 
                  max_prompt_length : int = 512,
                  beta : float = 0.0,
                  reward_weights : List[float] = None
                  ):

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
            gradient_accumulation_steps = 4, # Increase to 4 for smoother training
            num_generations = 2, # Decrease if out of memory
            max_prompt_length = max_prompt_length,
            max_completion_length = self.max_seq_len - max_prompt_length,
            # num_train_epochs = 1, # Set to 1 for a full training run
            max_steps = max_steps,
            save_steps = 250,
            max_grad_norm = 1.0,
            report_to = "none", 
            output_dir = output_dir,
            beta=beta,
            reward_weights= reward_weights
        )
        trainer = GRPOTrainer(
            model = self.model,
            processing_class = self.tokenizer,
            reward_funcs = reward_functions,
            args = training_args,
            train_dataset = dataset,
        )
        
        trainer.train()
        self.model.save_lora(saved_model_name)




    def generate_inference(self,
                           base_task_prompt : str,
                           system_prompt : str,
                           top_p : float = 0.95,
                           min_p = 0.1,
                           num_sequences : int = 10,
                           temperature : float = 0.7,
                           max_seq_len : int = 4196):
        

        def extract_xml_answer(text : str):
            answer = text.split("<output>")[-1]
            answer = answer.split("</output>")[0]
            return answer.strip()
        
        prompt_ = [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": base_task_prompt},
        ]

        if not self.use_vllm:

            inputs = self.tokenizer.apply_chat_template(prompt_, return_tensors="pt", add_generation_prompt=True).to(self.model.device)
            input_len = inputs.shape[1]

            outputs = self.model.generate(
                inputs,
                do_sample=True,
                temperature=temperature,
                top_p=top_p,
                min_p=min_p,
                max_new_tokens=max_seq_len,
                num_return_sequences = num_sequences,
                pad_token_id=self.tokenizer.pad_token_id
            )

            outputs = [self.tokenizer.decode(outputs[i, input_len:], skip_special_tokens=True).strip() for i  in range(len(outputs))]
            
            decoded_outputs = []
            for output in outputs:
                decoded_output = {
                                "prompt_with_think" : output,
                                "prompt" : extract_xml_answer(output)
                    }
                
                decoded_outputs.append(decoded_output)

        else:

            text = self.tokenizer.apply_chat_template(
                prompt_,
                add_generation_prompt = True, # Must add for generation
                tokenize = False,
            )

            

            decoded_outputs = []
            for _ in tqdm(range(num_sequences)):
                sampling_params = SamplingParams(
                    temperature = temperature,
                    top_p = top_p,
                    max_tokens = max_seq_len,
                    seed = random.randint(0, 1000000001)
                )
                output = self.model.fast_generate(
                            text,
                            sampling_params = sampling_params
                        )[0].outputs[0].text

                # print(f"Outputs = {output}")
                # print(f"\n\n")
                output = {
                                "prompt_with_think" : output,
                                "prompt" : extract_xml_answer(output)
                    }

                decoded_outputs.append(output)


        return decoded_outputs
    

    def get_best_inference_reward(self, 
                             sequences : List[str], 
                             context : str, 
                             answer_list : List[str], 
                             rewards : RewardFuncs,
                             topk : int):
        
        completions = [[{"content": sequence }] for sequence in sequences]

        special_token_reward = rewards.special_token_reward(completions=completions)
        exact_structure_reward = rewards.exact_structure_reward(completions = completions)
        format_reward = rewards.answer_format_reward(completions=completions, context = context)
        factoid_reward = rewards.factoid_ans_reward(completions=completions, context = context)
        # span_presence_reward = rewards.span_presence_reward(completions = completions, context=context)
        # correct_reward = rewards.correctness_reward(completions=completions, answer=answer_list, context = context)

        ########## Optional choice by output string length ###############
        len_reward = rewards.long_output_reward(completions=completions)

        net_reward = [
            sp_ + ex_ + form_ + fact_ + l_ 
            for sp_, ex_, form_, fact_, l_ in zip(
                special_token_reward, 
                exact_structure_reward, 
                format_reward, 
                factoid_reward,
                len_reward     
            )
        ]
        
        sequences = [(sequence, reward_) for sequence, reward_ in zip(sequences, net_reward)]
        sequences = sorted(sequences, key = lambda x : x[1], reverse = True)

        return sequences[:topk]






        

