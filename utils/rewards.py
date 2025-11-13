import re
from utils.generate import OClientModel, OModelConfig
    
######################### Reward Functions ###########################

class RewardFuncs:
    def __init__(self, ollama_model : OClientModel, ollama_config : OModelConfig, max_extractive_ans_len : int):
        self.ollama_model = ollama_model
        self.ollama_config = ollama_config
        self.max_extractive_ans_len = max_extractive_ans_len
        self.think_len_threshold = 256
        self.output_len_threshold = 256

    
    def extract_xml_tag(self, text : str, tag : str):
        think = text.split(f"<{tag}>")[-1]
        think = think.split(f"</{tag}>")[0]
        return think.strip()
    

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
            "refined prompt"
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
            "<refined prompt>", "</refined prompt>"
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
            "refined prompt"
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
    

    def answer_format_reward(self, completions, context, **kwargs):
        """
        Reward Function:
            The prompt when tested on another model should have the answer format,
            Answer: <answer string>
            Explantion: <explanation string>

            Answer: <answer string>
            Explanation: <explnation string>
        """
        completions = [f"Instruction:{self.extract_xml_answer(completion[0]["content"])}\nContext:{context_}" for context_, completion in zip(context,completions)]
        
        responses = [self.ollama_model(completion, **self.ollama_config.__dict__).response for completion in completions]
        self.ollama_responses = [response for response in responses]
        
        parsed_responses = [self.soft_parse_ollama(text) for text in responses]

        rewards = []
        for response in parsed_responses:
            if len(response) == 0:
                rewards.append(0.0)
            else:
                rewards.append(2.0)

        return rewards
    

    def factoid_ans_reward(self, completions, context, **kwargs):
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
                if len(resp_[0].split()) <= self.max_extractive_ans_len:
                    sample_reward += 1.0

            if len(response) > 0:
                rewards.append(sample_reward/len(response))
            else:
                rewards.append(0.0)

        return rewards
    

    def span_presence_reward(self, completions, context, **kwargs):
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
    

    def correctness_reward(self, completions, answer, context, **kwargs):
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
    
    def long_output_reward(self, completions, **kwargs):
        completions = [completion[0]["content"] for completion in completions]

        rewards = []

        for completion in completions:
            completion = self.extract_xml_answer(completion)
            if len(completion.replace("\n"," ").strip().split(" ")) >= 150:
                rewards.append(2.0)
            else:
                rewards.append(-1.0)

        return rewards
    

############################## Example of more rewarding strategies #######################################

class CreativeRewardFuncs(RewardFuncs):
    def __init__(self, ollama_model, ollama_config, max_extractive_ans_len):
        super().__init__(ollama_model, ollama_config, max_extractive_ans_len)


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

            if "<answer diversity analysis>" in text:
                reward += 0.25
            else:
                reward -= 1.0

            if "</answer diversity analysis>" in text:
                reward += 0.25
            else:
                reward -= 1.0

            if "<refined prompt>" in text:
                reward += 0.25
            else:
                reward -= 1.0
            
            if "</refined prompt>" in text:
                reward += 0.25
            else:
                reward -= 1.0

            rewards.append(reward)
        return rewards
    

    def exact_structure_reward(self, completions, **kwargs):
        """
        Reward Function: Checks if the completion adheres exactly to the required 
        four-section XML structure defined in the system prompt.
        
        Structure required:
        <think>...</think>
        <answer diversity analysis>...</answer diversity analysis>
        <refined prompt>...</refined prompt>
        """
        completions_text = [completion[0]["content"] for completion in completions]

        TAGS = {
            "think": ("<think>", "</think>"),
            "diversity_analysis": ("<answer diversity analysis>", "</answer diversity analysis>"),
            "refined_prompt": ("<refined prompt>", "</refined prompt>")
        }
        
        pattern_start = r"^[\s]*"
        pattern_think = rf"{re.escape(TAGS['think'][0])}\n(.+?)\n{re.escape(TAGS['think'][1])}[\s]*"
        pattern_diversity = rf"{re.escape(TAGS['diversity_analysis'][0])}\n(.+?)\n{re.escape(TAGS['diversity_analysis'][1])}[\s]*"
        pattern_refined = rf"{re.escape(TAGS['refined_prompt'][0])}\n(.+?)\n{re.escape(TAGS['refined_prompt'][1])}[\s]*"
        pattern_end = r"$"

        full_pattern = (
            pattern_start + 
            pattern_think + 
            pattern_diversity + 
            pattern_refined + 
            pattern_end
        )

        match_format = re.compile(
            full_pattern, 
            flags=re.MULTILINE | re.DOTALL
        )

        # --- Test the regex and assign rewards ---
        rewards = []
        for text in completions_text:
            reward = 0.0
            # Use fullmatch to ensure the entire text adheres to the pattern from start to finish
            match = match_format.fullmatch(text)
            if match:
                reward = 1.0

            rewards.append(reward)

        return rewards
            