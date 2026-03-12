import datasets
from tqdm import tqdm
from collections import defaultdict
from datasets import load_from_disk, load_dataset, concatenate_datasets


def reference_to_str(ref_dict : dict):
    output = ""
    for ref_ in ref_dict:
        output += ref_["title"] + ":\n" + ref_["content"] + "\n"

    output = output.strip()
    return output

def testcase_to_str(testcase : dict):

    sections = {
        "Test Purpose": "",
        "Initial Condition": "",
        "Test Procedure": "",
        "Expected Outcome": ""
    }

    for sec_ in testcase:
        if sec_["title"] == "Purpose":
            sections["Test Purpose"] = sec_["content"]

        if sec_["title"] == "Initial Conditions":
            sections["Initial Condition"] = sec_["content"]

        if sec_["title"] == "Steps/Description":
            sections["Test Procedure"] = sec_["content"]

        if sec_["title"] == "Expected Results":
            sections["Expected Outcome"] = sec_["content"]

    output = ""
    for title, content in sections.items():
        output += f"{title}:\n{content}\n\n"
    output = output.strip()
    return output


if __name__ == "__main__":
    augmented_dataset = defaultdict(list)
    combined_dataset_path = "Datasets/Testcase_Generation_Data.hf"


    bluetooth_paths = ["Datasets/Generic_Extractions/AVRCP/bluetooth_1.hf",
                        "Datasets/Generic_Extractions/BAP/bluetooth_2.hf",
                        "Datasets/Generic_Extractions/HFP/bluetooth_3.hf"
                        ]
    
    mozilla_paths = [
        "Datasets/Generic_Extractions/Mozilla_R1/Mozilla_R1.hf",
        "Datasets/Generic_Extractions/Mozilla_R2/Mozilla_R2.hf",
        "Datasets/Generic_Extractions/Mozilla_R3/Mozilla_R3.hf",
        "Datasets/Generic_Extractions/Mozilla_R4/Mozilla_R4.hf"
    ]

    bluetooth_datasets = concatenate_datasets([load_from_disk(path) for path in bluetooth_paths])
    mozilla_datasets = concatenate_datasets([load_from_disk(path) for path in mozilla_paths])

    print(bluetooth_datasets)
    print(mozilla_datasets)

    augmented_samples = defaultdict(list)

    for idx in tqdm(range(len(bluetooth_datasets))):
        augmented_samples["references"].append(bluetooth_datasets[idx]["references"])
        augmented_samples["testcase"].append(bluetooth_datasets[idx]["testcase"])
        augmented_samples["feature"].append(f"{bluetooth_datasets[idx]["name"]} {bluetooth_datasets[idx]["feature"]}")
        augmented_samples["source"].append("bluetooth")


    for idx in tqdm(range(len(mozilla_datasets))):
        augmented_samples["references"].append(reference_to_str(mozilla_datasets[idx]["reference"]))
        augmented_samples["testcase"].append(testcase_to_str(mozilla_datasets[idx]["testcase"]))
        augmented_samples["feature"].append(f"{mozilla_datasets[idx]["feature"]} {mozilla_datasets[idx]["sub_feature"]}".strip())
        augmented_samples["source"].append("mozilla")

    augmented_samples = datasets.Dataset.from_dict(augmented_samples)
    augmented_samples = augmented_samples.train_test_split(test_size=0.3, seed=42)

    augmented_samples.save_to_disk(combined_dataset_path)

    


    

