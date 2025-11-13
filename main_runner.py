import argparse
from functools import partial
from utils.rl_ans_trainer import RLEntityPRL
from utils.prepare_dataset import RLAnsDataset
from utils.generate import OClientModel, OModelConfig
from utils.rewards import RewardFuncs, CreativeRewardFuncs

def main():
    """
    Main training function to be executed by accelerate.
    """

    parser = argparse.ArgumentParser("RLHF Trainer arguments")
    parser.add_argument("--ollama_model_name", type=str, help="ollama model name")
    parser.add_argument("--port", help="ollama port", type=str)
    parser.add_argument("--policy_model_name", type=str, help="Policy model", default="unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit")
    parser.add_argument("--main_data", type = str, help = "dataset name", default="rajpurkar/squad")
    parser.add_argument("--max_factoid_len", type=int, help="factoid ans len", default=8)
    parser.add_argument("--max_seq_len", type = int, default=8192, help = "Maximum Sequence Length")
    parser.add_argument("--lora_rank", type=int, help="Lora Rank", default=64)
    parser.add_argument("--saved_model_name", type=str, help="Saved model name")
    parser.add_argument("--num_train_samples", type=int, help="num train samples")
    parser.add_argument("--train_steps", type=int, help="Num Training steps", default=500)
    parser.add_argument("--max_prompt_len", type=int, help="max prompt length", default=512)
    parser.add_argument("--output_dir", type = str, help = "Checkpoint save path")
    parser.add_argument("--beta", type = float, default=0.0, help = "KL penalty beta")
    parser.add_argument("--creative", action="store_true", help = "enable creative mode")

    args = parser.parse_args()

    model = OClientModel(model_name=args.ollama_model_name, port=args.port)
    config = OModelConfig()

    system_prompt = """You are an automative expert who specializes in generating diverse and effective prompts for generating test specifications for another model. Your primary goal is to analyze a given purpose and requirements, generate a *new, refined prompt* that aims to elicit a different, yet highly effective, set of answers.

Your entire response MUST follow a strictly defined structure with four main sections enclosed in specific tags:

1.  **<think>...</think>**: Detail your reasoning and analyze how to build the prompt.
2.  **<requirement analysis>...</requirement analysis>**: Provide an analysis of the requirements in the inputs from the expected output.
3.  **<verification analysis>...</verification analysis>**: Provide an analysis of the verification criteria present in the inputs from the expected output.
4.  **<quality analysis>...</quality analysis>**: Provide an analysis how quality of new prompt should be judged.
5.  **<output structure analysis>...</output structure analysis>**: Provide an analysis for the output structure in the output.
6.  **<prompt>...</prompt>**: Provide your new refined prompt.

### Response Format:

<think>
[Detailed analysis of the base prompt and strategy for refinement goes here. Focus on identifying and mitigating narrow focus or low diversity in potential answers.]
</think>
<requirement analysis>
[Analysis of the requirements in the inputs, focusing on testable parameters and completeness.]
</requirement analysis>
<verification analysis>
[Analysis of the necessary verification criteria, emphasizing measurability and pass/fail conditions.]
</verification analysis>
<quality analysis>
[Analysis of how the new prompt's quality should be judged (e.g., novelty, specificity, utility of the generated output).]
</quality analysis>
<output structure analysis>
[Analysis of the mandatory structured output format (e.g., JSON, Markdown table) required from the final prompt.]
</output structure analysis>
<prompt>
[The complete, actionable new prompt string goes here.]
</prompt>"""
        
    base_task_prompt = """Given an input and output pair, produce the prompt that produced the output for the input.
<input>
{}
</input>
<output>
{}
</output>"""

    if not args.creative:
        rewards = RewardFuncs(ollama_model = model, ollama_config=config, max_extractive_ans_len=int(args.max_factoid_len))
    else:
        rewards = CreativeRewardFuncs(ollama_model=model, ollama_config=config, max_extractive_ans_len=int(args.max_factoid_len))

    reward_functions = [
                        rewards.special_token_reward,
                        rewards.exact_structure_reward,
                        rewards.answer_format_reward,
                        rewards.factoid_ans_reward,
                        rewards.span_presence_reward,
                        rewards.correctness_reward
                        ]
    
    reward_weights = [1.0] * 6

    rl_entity_prl = RLEntityPRL(policy_model_name=args.policy_model_name, 
                                lora_rank=int(args.lora_rank),
                                max_seq_len=int(args.max_seq_len))
    
    rl_dataset = RLAnsDataset(data_name=args.main_data, num_samples = int(args.num_train_samples))
    train_dataset = rl_dataset.prepare_dataset(base_task_prompt=base_task_prompt, system_prompt=system_prompt)

    rl_entity_prl.train(reward_functions=reward_functions, 
                        saved_model_name = args.saved_model_name,
                        dataset = train_dataset,
                        output_dir = args.output_dir,
                        max_steps = int(args.train_steps),
                        max_prompt_length=int(args.max_prompt_len),
                        beta=float(args.beta), 
                        reward_weights=reward_weights)




if __name__ == "__main__":
    main()