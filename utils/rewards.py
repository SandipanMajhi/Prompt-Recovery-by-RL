import re
import json
from typing import List
from utils.generate import OClientModel, OModelConfig
    
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
            