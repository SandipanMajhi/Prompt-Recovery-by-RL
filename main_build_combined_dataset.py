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


# Maps each dataset path to its requirement specification label
BLUETOOTH_SPEC_MAP = {
    "Datasets/Generic_Extractions/AVRCP/bluetooth_1_v2.hf": "AVRCP Specification",
    "Datasets/Generic_Extractions/BAP/bluetooth_2_v2.hf":   "BAP Specification",
    "Datasets/Generic_Extractions/HFP/bluetooth_3_v2.hf":   "HFP Specification",
}

MOZILLA_SPEC_MAP = {
    "Datasets/Generic_Extractions/Mozilla_R1/Mozilla_R1.hf": "Mozilla Bookmarks Specification",
    "Datasets/Generic_Extractions/Mozilla_R2/Mozilla_R2.hf": "Mozilla Themes Specification",
    "Datasets/Generic_Extractions/Mozilla_R3/Mozilla_R3.hf": "Mozilla Password Manager Specification",
    "Datasets/Generic_Extractions/Mozilla_R4/Mozilla_R4.hf": "Mozilla Browser History Specification",
}


if __name__ == "__main__":
    combined_dataset_path = "Datasets/Testcase_Generation_Data_Bluetooth_v2.hf"

    augmented_samples = defaultdict(list)

    # --- Bluetooth datasets ---
    for path, spec_label in BLUETOOTH_SPEC_MAP.items():
        dataset = load_from_disk(path)
        for idx in tqdm(range(len(dataset)), desc=f"Processing {spec_label}"):
            augmented_samples["references"].append(dataset[idx]["references"])
            augmented_samples["testcase"].append(dataset[idx]["testcase"])
            augmented_samples["feature"].append(f"{dataset[idx]['feature']} {dataset[idx]['name']}")
            augmented_samples["source"].append("bluetooth")
            augmented_samples["requirement_specification"].append(spec_label)

    # --- Mozilla datasets ---
    # for path, spec_label in MOZILLA_SPEC_MAP.items():
    #     dataset = load_from_disk(path)
    #     for idx in tqdm(range(len(dataset)), desc=f"Processing {spec_label}"):
    #         augmented_samples["references"].append(reference_to_str(dataset[idx]["reference"]))
    #         augmented_samples["testcase"].append(testcase_to_str(dataset[idx]["testcase"]))
    #         augmented_samples["feature"].append(f"{dataset[idx]['feature']} {dataset[idx]['sub_feature']}".strip())
    #         augmented_samples["source"].append("mozilla")
    #         augmented_samples["requirement_specification"].append(spec_label)

    augmented_samples = datasets.Dataset.from_dict(augmented_samples)
    augmented_samples = augmented_samples.train_test_split(test_size=0.7, seed=42)

    augmented_samples.save_to_disk(combined_dataset_path)