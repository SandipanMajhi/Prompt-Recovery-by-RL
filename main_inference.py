import argparse
from functools import partial
from utils.rl_ans_trainer import RLEntityPRL
from utils.prepare_dataset import RLAnsDataset
from utils.generate import OClientModel, OModelConfig
from utils.rewards import RewardFuncs


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Ans Extraction Inference Arguments")

    parser.add_argument("--policy_model_name", type = str, help = "Base Policy Model name", default="unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit")
    parser.add_argument("--lora_adapter_path", type = str, help = "Lora Adapter Path")
    parser.add_argument("--ollama_model_name", type=str, help="ollama model name")
    parser.add_argument("--port", help="ollama port", type=str)
    parser.add_argument("--main_data", type = str, help = "dataset name", default="rajpurkar/squad")
    parser.add_argument("--max_factoid_len", type=int, help="factoid ans len", default=8)
    parser.add_argument("--max_seq_len", type = int, default=8192, help = "Maximum Sequence Length")
    parser.add_argument("--lora_rank", type=int, help="Lora Rank", default=64)
    parser.add_argument("--temperature", type = float, default = 0.7)
    parser.add_argument("--top_p", type = float, default = 0.9)
    parser.add_argument("--num_sequences", type = int, default=50)
    parser.add_argument("--seed", type = int, default=42)
    parser.add_argument("--topk", type = int, default = 20)


    args = parser.parse_args()

    model = OClientModel(model_name=args.ollama_model_name, port=args.port)
    config = OModelConfig()


    system_prompt = """A conversation between User and Assistant. The user gives a task, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides the user
with the output. The reasoning process must be enclosed within <think> </think> tags and the output must be enclosed within <output> </output> tags, i.e., the format should be,
<think>
reasoning process here.
</think>
<output>
output here 
</output>"""
        
    base_task_prompt = """Your task is to refine a base prompt for another model that performs answer extraction from a context provided externally by the user. Improve the base prompt to enhance the model's performance. You must ensure that the instruction must include output format for the another model.
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

    rewards = RewardFuncs(ollama_model = model, ollama_config=config, max_extractive_ans_len=int(args.max_factoid_len))
    rl_entity_prl = RLEntityPRL(policy_model_name=args.policy_model_name, 
                                lora_rank=int(args.lora_rank),
                                max_seq_len=int(args.max_seq_len), 
                                is_inference=True,
                                lora_adapter_name=args.lora_adapter_path,
                                use_vllm=True)
    
    rl_dataset = RLAnsDataset(data_name=args.main_data, num_samples = 3000)
    train_dataset = rl_dataset.prepare_dataset(base_task_prompt=base_task_prompt, system_prompt=system_prompt)
    
    generated_sequences = rl_entity_prl.generate_inference(base_task_prompt=base_task_prompt,
                                                           system_prompt=system_prompt,
                                                           num_sequences=int(args.num_sequences), 
                                                           temperature=float(args.temperature),
                                                           top_p=float(args.top_p),
                                                           max_seq_len=int(args.max_seq_len))

    sequences = [seq["prompt_with_think"] for seq in generated_sequences]

    top_k_sequences = rl_entity_prl.get_best_inference_reward(sequences=sequences, 
                                                              context=train_dataset[0]["context"], 
                                                              answer_list=train_dataset[0]["answer"], 
                                                              rewards=rewards, 
                                                              topk=int(args.topk) )
    
    """
        top_k_sequences: List of tuple (sequence_prompt, reward)
    """
    

    for seq in top_k_sequences:
        print(seq[0])
        print(seq[1])

        print("\n\n")





    
     




