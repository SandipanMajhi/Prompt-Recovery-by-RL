import argparse
import yaml
from pathlib import Path
from functools import partial
from utils.rl_trainer import PRLTrainer
from utils.prepare_dataset import PromptOptimDataset
from utils.generate import OClientModel, OModelConfig, OClientModelv2
from utils.rewards import RewardFuncsv2

def main():
    """
    Main training function to be executed by accelerate.
    """

    with open("Configurations/PromptOptim_Trainerv1.yaml", "r") as file:
        config = yaml.safe_load(file)

    dir_path = Path(config["output_dir"])
    dir_path.mkdir(parents = True, exist_ok=True)

    model = OClientModel(model_name=config["ollama_model_name"], port=config["port"])
    # model = OClientModelv2(model_name = config["ollama_model_name"], port = config["port"])
    model_config = OModelConfig()
    # model_config = OModelConfig(think="low")

    system_prompt = """A conversation between User and Assistant. The user gives a task, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user
with the output. The reasoning process must be enclosed within <think> </think> tags and the output must be enclosed within <output> </output> tags, i.e., the format should be,
<think>
reasoning process here.
</think>
<output>
output here 
</output>"""
        
    base_task_prompt = """You are an advanced Prompt Engineering Assistant specializing in QA Engineering and Test Automation specializing in Bluetooth.
Your primary goal is to analyze a given base prompt prefix and generate a new refined prompt prefix that aims to elicit a proper test case for the feature. You only have to generate the refined prefix prompt. 
Please do not generate any few-shot examples with arbitrary reference, feature, test case name and items. 

Constraints:
- Do not generate any few-shot examples.
- Do not provide reference, feature, test case name and items.
- Output ONLY the refined prompt prefix.

Base Task prompt prefix: Given the following feature, test case name, item and references you have to design testcases for it. 
Your test case must have the following sections section title, Test Purpose, Initial Condition, Test Procedure and Expected Outcome.

Output Format:
### Test Purpose:
<content>

### Initial Condition:
<content>

### Test Procedure:
<content>

### Expected Outcome:
<content>

Only output your test case in the above output format with sections mentioned in markdown format and nothing else.

New Refined Prompt Prefix:"""

    
    rewards = RewardFuncsv2(ollama_model = model, ollama_config=model_config)

    reward_functions = [
                        rewards.answer_format_reward,
                        rewards.think_length_reward, 
                        rewards.output_length_reward,
                        rewards.section_presence_reward,
                        rewards.sectionwise_overlap_reward,
                        rewards.keyword_overlap_reward,
                        rewards.special_token_reward
                        ]
    
    reward_weights = [1.0] * 7

    rl_prl = PRLTrainer(policy_model_name=config["policy_model_name"], 
                                lora_rank=int(config["lora_rank"]),
                                max_seq_len=int(config["max_seq_len"]))
    
    rl_dataset = PromptOptimDataset(num_samples=int(config["num_train_samples"]))
    train_dataset = rl_dataset.prepare_dataset(user_prompt=base_task_prompt, system_prompt=system_prompt, data_paths=config["data_paths"])

    rl_prl.train(reward_functions=reward_functions, 
                        saved_model_name = config["saved_model_name"],
                        dataset = train_dataset,
                        output_dir = config["output_dir"],
                        max_steps = int(config["train_steps"]),
                        max_prompt_length=int(config["max_prompt_len"]),
                        beta=float(config["beta"]), 
                        reward_weights=reward_weights)




if __name__ == "__main__":
    main()