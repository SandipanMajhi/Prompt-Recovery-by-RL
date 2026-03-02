import datasets 
from datasets import load_from_disk
from tqdm import tqdm
import pickle as pkl
import json
import re


def gold_testcase_parser(text : str):
    headers = ["Test Purpose", "Initial Condition", "Test Procedure", "Expected Outcome"]
    pattern = "|".join(headers)
    regex_pattern = rf"({pattern}):\s*(.*?)(?=\n(?:{'|'.join(headers)}):|$)"
    matches = re.findall(regex_pattern, text, re.DOTALL)
    extracted_data = {header.strip(): content.strip() for header, content in matches}
    return extracted_data



if __name__ == "__main__":

    # with open("Datasets/Generic_Extractions/VDP/bluetooth_4.pkl", "rb") as fp:
    #     samples = pkl.load(fp)

    # num_samples = len(samples["testcases"])

    # id = 4

    # print(samples["references"][id])
    # print("\n\n")
    # print(samples["testcases"][id])
    # print("\n\n")
    # print(samples["item"][id])
    # print("\n\n")
    # print(samples["feature"][id])
    # print("\n\n")
    # print(samples["test_cases_ids"][id])

    # samples = load_from_disk("Datasets/Generic_Extractions/Mozilla_R4/Mozilla_R4_GPT_OSS_20b_references.hf")
    samples = load_from_disk("Datasets/Generic_Extractions/AVRCP/bluetooth_1.hf")

    print(samples)
    print(samples[0])
    
    # for idx in tqdm(range(len(samples))):
    #     print(f"IDX = {idx}")
    #     # print(samples["references"][idx])
    #     # print(samples["gpt_oss_references"][idx])
    #     # print(json.loads(samples["gpt_oss_references"][idx]))
    #     print("\n\n")
    #     print(gold_testcase_parser(samples["testcase"][idx]))
    #     # print(samples["testcase"][idx])
    #     print("\n\n")

    # print(samples[-1])

    # is_fintunable = 0
    # score = 0

    # print(samples)
    # print(samples[-1])

    # for idx in tqdm(range(len(samples))):
    #     analysis = samples[idx]["Analysis"]
    #     score += analysis["score"]

    #     if analysis["is_fine_tuning_ready"]:
    #         is_fintunable += 1
        

    # print(f"Average Dataset Score = {score/len(samples)}")
    # print(f"Ratio of finetunable examples = {is_fintunable/len(samples)}")


    