import datasets 
from datasets import load_from_disk
from tqdm import tqdm
import pickle as pkl



if __name__ == "__main__":

    samples = load_from_disk("Datasets/Generic_Extractions/Mozilla_R1/Mozilla_R1_GPT_OSS_20b_references.hf")
    print(samples)
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


    