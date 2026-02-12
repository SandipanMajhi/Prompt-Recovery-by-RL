import datasets 
from datasets import load_from_disk
from tqdm import tqdm



if __name__ == "__main__":
    samples = load_from_disk("Datasets/Generic_Extractions/generic_dataset_v1.hf")
    is_fintunable = 0
    score = 0

    print(samples)
    print(samples[-1])

    for idx in tqdm(range(len(samples))):
        analysis = samples[idx]["Analysis"]
        score += analysis["score"]

        if analysis["is_fine_tuning_ready"]:
            is_fintunable += 1
        

    print(f"Average Dataset Score = {score/len(samples)}")
    print(f"Ratio of finetunable examples = {is_fintunable/len(samples)}")


    