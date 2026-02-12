from utils.llm_judge import LLM_as_Judge
from utils.generate import OClientModel, OModelConfig
import json
from tqdm import tqdm
import argparse
from collections import defaultdict
from datasets import Dataset



if __name__ == "__main__":
    with open("Datasets/Generic_Extractions/tc_req.json", "r", encoding="utf-8") as fp:
        tc_req_dict = json.load(fp)

    with open("Datasets/Generic_Extractions/tc_edited.json", "r", encoding="utf-8") as fp:
        tc_dict = json.load(fp)

    model = OClientModel(model_name="gpt-oss:20b", port = "11434", seed = 42)
    model_config = OModelConfig()
    llm_judge = LLM_as_Judge(model = model, config = model_config)

    augmented_data = defaultdict(list)

    counter = 0

    for k,v in tqdm(tc_req_dict.items()):
        section_id = k 
        list_of_req = v

        testcase = None

        for tc_ in tc_dict:
            if tc_["section_id"] == k:
                testcase = tc_
                break

        testcase = json.dumps(testcase, indent=2)
        list_of_req = json.dumps(list_of_req, indent=2)

        if testcase is not None and len(testcase) > 0 and list_of_req is not None and len(list_of_req) > 0:

            output = llm_judge(tc = testcase, req=list_of_req)

            augmented_data["testcase"].append(testcase)
            augmented_data["requirements"].append(list_of_req)
            augmented_data["Analysis"].append(output)

            counter += 1

        if counter % 10 == 0:
            saved_data = Dataset.from_dict(augmented_data)
            saved_data.save_to_disk("Datasets/Generic_Extractions/generic_dataset_v1.hf")

    
    augmented_data = Dataset.from_dict(augmented_data)
    augmented_data.save_to_disk("Datasets/Generic_Extractions/generic_dataset_v1.hf")


        






         
        




    