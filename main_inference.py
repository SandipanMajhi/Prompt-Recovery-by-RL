import argparse
from functools import partial
from utils.rl_trainer import PRLTrainer
from utils.prepare_dataset import RLPRLDataset
from utils.generate import OClientModel, OModelConfig
from utils.rewards import RewardFuncs


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Ans Extraction Inference Arguments")

    parser.add_argument("--policy_model_name", type = str, help = "Base Policy Model name", default="unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit")
    parser.add_argument("--lora_adapter_path", type = str, help = "Lora Adapter Path")
    parser.add_argument("--ollama_model_name", type=str, help="ollama model name")
    parser.add_argument("--port", help="ollama port", type=str)
    parser.add_argument("--max_seq_len", type = int, default=16000, help = "Maximum Sequence Length")
    parser.add_argument("--max_prompt_len", type = int, default = 4196)
    parser.add_argument("--lora_rank", type=int, help="Lora Rank", default=64)
    parser.add_argument("--temperature", type = float, default = 0.7)
    parser.add_argument("--top_p", type = float, default = 0.9)
    parser.add_argument("--num_sequences", type = int, default=50)
    parser.add_argument("--seed", type = int, default=42)


    args = parser.parse_args()

    model = OClientModel(model_name=args.ollama_model_name, port=args.port)
    config = OModelConfig()


    system_prompt = """A conversation between User and Assistant. The user gives a task, and the Assistant solves it.
The assistant first thinks about the reasoning process in the mind and then provides the user with the output. 
The reasoning process must be enclosed within <think> </think> tags and the output must be enclosed within <output> </output> tags.

### Role
You are an expert Prompt Engineer specializing in Bluetooth QA and Test Automation. 

### Objective
Your goal is to optimize the provided "Base Task Prompt" into a "Refined Prompt Prefix." 
The refined version must elicit high-quality, technically rigorous Bluetooth test cases while maintaining the requested output format.

### Strict Constraints
1. NO few-shot examples (no sample features or test names).
2. NO arbitrary data or reference items.
3. The refined prompt MUST instruct the model to use the specific sections: Test Purpose, Initial Condition, Test Procedure, and Expected Outcome.
4. Output ONLY the refined prompt prefix inside the <output> tags.
"""
    base_task_prompt = """You are an advanced Prompt Engineering Assistant specializing in QA Engineering and Test Automation specializing in Bluetooth.
Your primary goal is to analyze the following base prompt and generate a refined prefix prompt. 

---
Base Task Prompt Prefix:
Given the following feature, test case name, item and references you have to design testcases for it. 
Your test case must have the following sections section title, Test Purpose, Initial Condition, Test Procedure and Expected Outcome.

You must produce your test case in the following format.
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


    prl = PRLTrainer(policy_model_name=args.policy_model_name, 
                                lora_rank=int(args.lora_rank),
                                max_seq_len=int(args.max_seq_len), 
                                is_inference=True,
                                lora_adapter_name=args.lora_adapter_path,
                                use_vllm=True)
    
    generated_sequences = prl.generate_inference(base_task_prompt=base_task_prompt,
                                                           system_prompt=system_prompt,
                                                           num_sequences=int(args.num_sequences), 
                                                           temperature=float(args.temperature),
                                                           top_p=float(args.top_p),
                                                           max_seq_len=int(args.max_seq_len))

    sequences = [seq["prompt_with_think"] for seq in generated_sequences]
    

    for seq in sequences:
        print(seq)
        print("\n\n\n")





    
     




