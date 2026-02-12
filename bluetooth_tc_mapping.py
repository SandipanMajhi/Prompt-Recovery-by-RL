from utils.build_dataset import AVRCPmd
import json
from collections import defaultdict
import datasets
from tqdm import tqdm
import pickle as pkl


def search_tc(tc_req_json:dict):
    pass


if __name__ == "__main__":

    base_path = "Datasets/Generic_Extractions/VDP"
    tc_req_json_path = "Datasets/Generic_Extractions/VDP/tc_req.json"
    tc_json_path = "Datasets/Generic_Extractions/VDP/tc.json"
    tc_mapping_md_path = "Datasets/Generic_Extractions/VDP/tc_mapping.md"
    hf_path = "Datasets/Generic_Extractions/VDP/bluetooth_4.pkl"


    with open(tc_req_json_path, "r", encoding="utf-8") as fp:
        tc_req_json = json.load(fp)

    with open(tc_json_path, "r", encoding="utf-8") as fp:
        tc_json = json.load(fp)

    with open(tc_mapping_md_path, "r") as fp:
        tc_mapping_md = fp.read()

    tc_mappings = AVRCPmd.tc_mapping_read(tc_map_md=tc_mapping_md)

    augmented_samples = defaultdict(list)
    for mapping in tqdm(tc_mappings):
        
        test_cases = mapping["test_cases"]

        all_references = []
        all_test_cases = []

        for tc_ in test_cases:
            reference = {}
            original_test_case = {}

            for tc_id, tc_req_ in tc_req_json.items():
                if tc_ == tc_id:
                    reference = tc_req_
                    break 

            for tc_d in tc_json:
                if tc_ == tc_d["section_id"]:
                    original_test_case = tc_d
                    break
            
            if len(reference) > 0:
                all_references.append(reference)
            
            if len(original_test_case) > 0:
                all_test_cases.append(original_test_case)

        augmented_samples["references"].append(all_references)
        augmented_samples["testcases"].append(all_test_cases)
        augmented_samples["item"].append(mapping["item"])
        augmented_samples["feature"].append(mapping["feature"])
        augmented_samples["test_cases_ids"].append(mapping["test_cases"])

    with open(hf_path, "wb") as fp:
        pkl.dump(augmented_samples, fp)

    # print(augmented_samples)
    # augmented_samples = datasets.Dataset.from_dict(augmented_samples)
    # augmented_samples.save_to_disk(hf_path)





    

    
