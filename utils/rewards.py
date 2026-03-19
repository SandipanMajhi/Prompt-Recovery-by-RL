import re
import uuid
import random
import json
from typing import List
from utils.generate import OClientModel, OModelConfig, OClientModelv2
from typing import Union, List
import evaluate
    
######################### Reward Functions ###########################

class RewardFuncs:
    def __init__(self, ollama_model : OClientModel, ollama_config : OModelConfig):
       

        self.ollama_model = ollama_model
        self.ollama_config = ollama_config
       

    
    def extract_xml_tag(self, text : str, tag : str):
        think = text.split(f"<{tag}>")[-1]
        think = think.split(f"</{tag}>")[0]
        return think.strip()
    

    def isJSON(self, text : str):
        if not isinstance(text, str):
            return text, False
        
        try:
            json_dict = json.loads(text)
            return json_dict, True
        except json.JSONDecodeError:
            return None, False
        except TypeError:
            return None, False
            
    

    def soft_parse_ollama(self, generated_text: str) -> dict:
        """
        Parser to extract the content from the six required sections 
        (enclosed in XML-like tags) of the refined prompt generation output.
        """
        results = {}
        tags = [
            "think",
            "requirement analysis",
            "verification analysis",
            "quality analysis",
            "output structure analysis",
            "prompt"
        ]

        for tag in tags:
            pattern = re.compile(
                rf"<{re.escape(tag)}>(.*?)</{re.escape(tag)}>", 
                re.IGNORECASE | re.DOTALL
            )
            
            match = pattern.search(generated_text)
            
            if match:
                content = match.group(1).strip()
                results[tag] = content
            else:
                results[tag] = None
                
        return results


    def special_token_reward(self, completions, **kwargs):
        """
        Reward Function: 
        To check the output of the policy model to see if it contains all six pairs of 
        required structure tags: <think>, <requirement analysis>, 
        <verification analysis>, <quality analysis>, <output structure analysis>, 
        and <refined prompt> (assuming 'refined prompt' from context).
        """
        required_tags = [
            "<think>", "</think>",
            "<requirement analysis>", "</requirement analysis>",
            "<verification analysis>", "</verification analysis>",
            "<quality analysis>", "</quality analysis>",
            "<output structure analysis>", "</output structure analysis>",
            "<prompt>", "</prompt>"
        ]
        
        completions = [completion[0]["content"] for completion in completions]
        
        rewards = []
        
        
        TAG_REWARD = 0.5 
        TAG_PENALTY = -1.0 

        for text in completions:
            reward = 0.0
            
            for tag in required_tags:
                if tag in text:
                    reward += TAG_REWARD
                else:
                    reward += TAG_PENALTY
            
            rewards.append(reward)
            
        return rewards
    

    def exact_structure_reward(self, completions, **kwargs):
        """
        Reward Function:
        Checks if the completion exactly follows the strict sequential format 
        of all six required sections: <think>, <requirement analysis>, 
        <verification analysis>, <quality analysis>, <output structure analysis>,
        and <refined prompt>.
        
        A high reward (1.0) is given only if the *entire* completion matches 
        this required structure and order.
        """
        completions = [completion[0]["content"] for completion in completions]
        rewards = []

        tags = [
            "think", 
            "requirement analysis", 
            "verification analysis", 
            "quality analysis", 
            "output structure analysis", 
            "prompt"
        ]
        
        pattern_parts = [r"^[\s]*"]
        
        for tag in tags:
            block_pattern = (
                rf"<{re.escape(tag)}>"
                r".*?"
                rf"</{re.escape(tag)}>"
                r"[\s]*"
            )
            pattern_parts.append(block_pattern)

        pattern_parts.append(r"$")
        full_pattern = "".join(pattern_parts)
        
        match_format = re.compile(
            full_pattern,
            flags=re.MULTILINE | re.DOTALL
        )

        for text in completions:
            reward = 0.0
            match = match_format.search(text)
            
            if match:
                reward = 1.0
            else:
                reward = 0.0

            rewards.append(reward)

        return rewards
    

    def answer_verification_reward(self, completions, input_instruction, **kwargs):
        """
            Check the output of the new prompt.
        """
        new_prompts = [self.extract_xml_tag(text=completion[0]["content"], tag="prompt")  for completion in completions]
        new_prompts = [ f"{prompt_}\nTask:{inst_}"   for inst_, prompt_ in zip(input_instruction, new_prompts)]

        responses = [self.ollama_model(prompt_, **self.ollama_config.__dict__) for prompt_ in new_prompts]

        rewards = []
        for response in responses:
            reward_ = 0.0
            json_response, is_json = self.isJSON(text=response)
            if not is_json:
                reward_ += -1.0
            else:
                reward_ += 1.0

                if "preconditions" in json_response:
                    reward_ += 0.3 

                if "action_steps" in json_response:
                    reward_ += 0.3 

                if "postconditions" in json_response:
                    reward_ += 0.3 


            rewards.append(reward_)

        return rewards



class RewardFuncsv2(RewardFuncs):
    def __init__(self, 
                 ollama_model : Union[OClientModel, OClientModelv2], 
                 ollama_config : OModelConfig,
                 think_length_threshold : int = 150,
                 output_length_threshold : int = 150,  
                 tags : List[str] = None):
        super().__init__(ollama_model, ollama_config)

        if tags is None:
            self.tags = ["Test Purpose", 
                    "Initial Condition", 
                    "Test Procedure", 
                    "Expected Outcome"]
        else:
            self.tags = tags

        self.think_length_threshold = think_length_threshold
        self.output_length_threshold = output_length_threshold

        self.experiment_id = uuid.uuid4()
        self.rouge_scorer = evaluate.load("rouge", experiment_id=self.experiment_id)



    def extract_xml_tag(self, text : str, tag : str):
        text = text.split(f"<{tag}>")[-1]
        text = text.split(f"</{tag}>")[0]
        return text.strip()
    
    def gold_testcase_parser(self, text : str):
        headers = ["Test Purpose", "Initial Condition", "Test Procedure", "Expected Outcome"]
        pattern = "|".join(headers)
        regex_pattern = rf"({pattern}):\s*(.*?)(?=\n(?:{'|'.join(headers)}):|$)"
        matches = re.findall(regex_pattern, text, re.DOTALL)
        extracted_data = {header.strip(): content.strip() for header, content in matches}
        return extracted_data
    

    def response_parser(self, text : str):
        pattern = r"### (.*?):\s*(.*?)(?=###|$)"
        matches = re.findall(pattern, text, re.DOTALL)
        parsed_data = {header.strip(): content.strip() for header, content in matches}
        return parsed_data
    
    def output_length_reward(self, completions, **kwargs):
        completions = [self.extract_xml_tag(completion[0]["content"], tag="output") for completion in completions]
        rewards = []

        for out_response in completions:
            if len(out_response.split()) > self.output_length_threshold:
                rewards.append(2.0)
            else:
                rewards.append(-1.0)

        return rewards

        
    
    def think_length_reward(self, completions, **kwargs):
        completions = [self.extract_xml_tag(completion[0]["content"], tag="think") for completion in completions]

        rewards = []

        for out_response in completions:
            if len(out_response.split()) > self.output_length_threshold:
                rewards.append(2.0)
            else:
                rewards.append(-1.0)

        return rewards
    


    def answer_format_reward(self, completions, feature, source, specification, reference,  **kwargs):

        def create_prompt(completion : str, 
                          ref_ :str, 
                          feat_ : str, 
                          source_ : str,
                          specification_ : str):
            
            output_format_prompt = """You must produce your test case in the following format.
### Test Purpose:
<test purpose content>

### Initial Condition:
<initial condition content>

### Test Procedure:
<test procedure content>

### Expected Outcome:
<expected outcome content>

Only output your test case in the above output format with sections mentioned in markdown format and nothing else.
---"""
            
            modified_prefix_prompt = f"""{completion}

{output_format_prompt}
            
Feature and Test Case Name: {feat_}
Item: {source_}
References: {specification_}\n\n{ref_}"""
            
            return modified_prefix_prompt

        completions = [self.extract_xml_tag(completion[0]["content"], tag="output") for completion in completions]
        # print(f"Completions = {completions}", flush = True)
        completions = [create_prompt(completion, ref_, feat_, source_, specification_) for completion, ref_, feat_, source_, specification_ in zip(completions, reference, feature, source, specification)]

        responses = [self.ollama_model(completion, **self.ollama_config.__dict__).response for completion in completions]
        self.ollama_responses = [response for response in responses]
        # print(f"Ollama Responses = {self.ollama_responses}", flush = True)

        rewards = []
        for response in self.ollama_responses:
            if len(response) == 0:
                rewards.append(0.0)
            else:

                rewards.append(2.0)

        return rewards
    

    def section_presence_reward(self, completions, **kwargs):
        parsed_responses = [self.response_parser(response) for response in self.ollama_responses]

        rewards = []
        for response in parsed_responses:
            if len(response) == len(self.tags) and all([key in response for key in self.tags]):
                rewards.append(2.0)
            else:
                rewards.append(-1.0)

        return rewards
    
    def sectionwise_overlap_reward(self, completions, testcase, **kwargs):
        parsed_responses = [self.response_parser(response) for response in self.ollama_responses]
        testcase = [self.gold_testcase_parser(tc_) for tc_ in testcase]

        rewards = []
        for response, gold_tc in zip(parsed_responses, testcase):
            if len(response) == len(self.tags):
                all_scores = []
                for tag in self.tags:
                    if tag in response and tag in gold_tc:
                        overlap_score = self.rouge_scorer.compute(predictions = [response[tag]], references= [gold_tc])["rougeL"]
                        all_scores.append(overlap_score)
                    else:
                        all_scores.append(0.0)

                rewards.append(sum(all_scores))
                    
            else:
                rewards.append(0.0)

        return rewards


    def keyword_overlap_reward(self, completions, testcase, **kwargs):

        def _compare(key_info_1 : List[str], key_info_2 : List[str]):
            """
                key_info_2 has to be reference
            """

            counts = 0

            for key_2 in key_info_2:
                for key_1 in key_info_1:
                    if self.rouge_scorer.compute(predictions = [key_1.lower()], references= [key_2.lower()] )["rougeL"] >= 0.5 : 
                        counts += 1
                        break

            return counts / len(key_info_2)
        
 
        def generate_keys(tc_ : str, num_trials : int = 1):
            prompt = f"""Given the following test case find out the key information.
A key information is a very short span (3-6 words) from the text which are very important factually. You must produce the list of key information in comma separated format only.

Output format: key1, key2, key3, key4 ... 

Test Case: {tc_}

Only output your key information in the prescribed format and nothing else."""
            
            all_outputs = []
        
            for _ in range(num_trials):
                config = OModelConfig(temperature=0.7, seed = random.randint(0, 34556))
                # config = OModelConfig(temperature=0.7, seed = random.randint(0, 34556), think="low")
                output = self.ollama_model(prompt, **config.__dict__).response
                output = output.split(",")
                output = [out.strip() for out in output]

                all_outputs.extend(output)

            all_outputs = list(set(all_outputs))
            return all_outputs

        parsed_responses = [self.response_parser(response) for response in self.ollama_responses]
        parsed_responses = [(response, tc_) for response, tc_ in zip(parsed_responses, testcase)]

        rewards = []

        for gen_response, gold_tc_ in parsed_responses:
            generated_keys = generate_keys(gen_response)
            gold_keys = generate_keys(gold_tc_)
            comparison_reward = _compare(generated_keys, gold_keys)
            rewards.append(comparison_reward * 2.0)

        return rewards
    

    def special_token_reward(self, completions, **kwargs):
        completions  = [completion[0]["content"] for completion in completions]

        rewards = []
        for response in completions:
            reward = 0.0

            if "<think>" in response:
                reward += 0.5

            if "</think>" in response:
                reward += 0.5

            if "<output>" in response:
                reward += 0.5

            if "</output>" in response:
                reward += 0.5

            rewards.append(reward)

        return rewards