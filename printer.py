import datasets 
from datasets import load_from_disk
from tqdm import tqdm
import pickle as pkl



if __name__ == "__main__":

    with open("Datasets/Generic_Extractions/VDP/bluetooth_4.pkl", "rb") as fp:
        samples = pkl.load(fp)

    num_samples = len(samples["testcases"])

    id = 4

    print(samples["references"][id])
    print("\n\n")
    print(samples["testcases"][id])
    print("\n\n")
    print(samples["item"][id])
    print("\n\n")
    print(samples["feature"][id])
    print("\n\n")
    print(samples["test_cases_ids"][id])

    # samples = load_from_disk("Datasets/Generic_Extractions/AVRCP/bluetooth_1.pkl")
    # print(samples)
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


    