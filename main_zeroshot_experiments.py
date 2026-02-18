import datasets
import re
import random
from tqdm import tqdm
import yaml
from pathlib import Path
from collections import defaultdict
from datasets import load_from_disk 
from utils.generate import OClientModel, OClientModelv2, OModelConfig


def parse_predicted(pred_ : str):
    pattern = r"### (.*?):\s*(.*?)(?=###|$)"
    matches = re.findall(pattern, pred_, re.DOTALL)
    parsed_data = {header.strip(): content.strip() for header, content in matches}
    return parsed_data


def parse_reference(ref_ : str):
    target_sections = [
        "Test Purpose", 
        "Initial Condition", 
        "Test Procedure", 
        "Expected Outcome"
    ]

    header_pattern = "|".join(map(re.escape, target_sections))
    pattern = rf"^({header_pattern}):\s*(.*?)(?=^(?:{header_pattern}):|\Z)"
    matches = re.finditer(pattern, ref_, re.MULTILINE | re.DOTALL)
    return {match.group(1).strip(): match.group(2).strip() for match in matches}


def generate_prompt(tc_name : str, reference : str, feature : str):
    prompt = f"""Given the following feature, test case name and references you have to design testcases for it. 
Your test case must have the following sections section title, Test Purpose, Initial Condition, Test Procedure and Expected Outcome.

Reference: {reference}

Test Case Name: {tc_name}

Feature: {feature}

Output Format:
### Test Purpose: <content>

### Initial Condition: <content>

### Test Procedure: <content>

### Expected Outcome: <content>

-----

Only output your test case in the above output format with sections mentioned in markdown format and nothing else."""
    
    return prompt


def key_information(tc_ : str, model : OClientModel, num_trials : int = 3):
    prompt = f"""Given the following test case find out the key information.
A key information is a very short span (3-6 words) from the text which are very important factually. You must produce the list of key information in comma separated format only.

Output format: key1, key2, key3, key4 ... 

Test Case: {tc_}

Only output your key information in the prescribed format and nothing else."""
    
    all_outputs = []
    
    for _ in range(num_trials):
        config = OModelConfig(temperature=0.7, seed = random.randint(0, 34556))
        output = model(prompt, **config.__dict__).response
        output = output.split(",")
        output = [out.strip() for out in output]

        all_outputs.extend(output)

    all_outputs = list(set(all_outputs))
    return all_outputs    





if __name__ == "__main__":
    with open("Configurations/zeroshot_test.yaml", "r") as file:
        config = yaml.safe_load(file)

    # dir_path = Path(config["output_folder"])
    # dir_path.mkdir(parents = True, exist_ok=True)

    model = OClientModel(model_name = config["model_name"], port = config["port"])
    model_config = OModelConfig(temperature=0.7)

    samples = load_from_disk(config["dataset_path"])
    print(samples)

    """
        Dataset({
            features: ['references', 'testcase', 'name', 'feature', 'item'],
            num_rows: 127
        })
    """

    for idx in tqdm(range(len(samples))):
        tc_name = samples["name"][idx]
        reference = samples["references"][idx]
        feature = samples["feature"][idx]
        testcase = samples["testcase"][idx]

        prompt = generate_prompt(tc_name=tc_name,
                                 reference=reference,
                                 feature = feature)
        
        output = model(prompt=prompt, **model_config.__dict__).response
        key_info = key_information(tc_= output, model = model, num_trials=3)
        key_info_tc = key_information(tc_ = testcase, model = model, num_trials=3)
        
        print(f"Model Response = {output}", flush = True)
        print("\n\n\n")

        print(f"Original TC = {testcase}", flush = True)
        print("\n\n\n")

        print(f"Parsed Model Response = {parse_predicted(output)}", flush= True)
        print("\n\n\n")

        print(f"Parsed Original TC = {parse_reference(testcase)}", flush= True)
        print("\n\n\n")

        print(f"Key Information = {key_info}", flush = True)
        print("\n\n")

        print(f"Key Information Gold = {key_info_tc}", flush= True)
        print("\n\n")

        break




