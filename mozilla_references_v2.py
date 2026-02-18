import datasets
from tqdm import tqdm 
from collections import defaultdict
from datasets import load_from_disk
import json
from typing import List, Dict
from utils.generate import OClientModelv2, OModelConfig


def ref_to_json(ref_ : str, model : OClientModelv2, config : OModelConfig):
    ref_ = ref_.replace("```json\n", "")
    ref_ = ref_.replace("```","")
    try:
        ref_ = json.loads(ref_)
        return ref_ 
    except:
        prompt = generate_prompt(text=ref_)
        output = model(prompt = prompt, **config.__dict__).response
        # print(f"GPT OSS json = {output}", flush = True)
        return output

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


def generate_prompt(text: str):
    prompt = f"""Given the following dictionary extract the title and content. For all title-content pair organise them into the following format, 
Answer Format: 
<Title1>:
<Content1>

<Title2>:
<Content2>

<Title3>:
<Content3>
    

Dict: {text}

Only output in the prescribed answer format and nothing else."""
    return prompt



if __name__ == "__main__":
    save_path = "Datasets/Generic_Extractions/Mozilla_R4/Mozilla_R4_final.hf"
    samples1 = load_from_disk("Datasets/Generic_Extractions/Mozilla_R4/Mozilla_R4_GPT_OSS_20b_references.hf")
    samples2 = load_from_disk("Datasets/Generic_Extractions/Mozilla_R4/Mozilla_R4.hf")

    print(samples1)
    print(samples2)

    model = OClientModelv2(model_name="gpt-oss:20b", port = "11434")
    config = OModelConfig(think = "low", temperature=0.7)

    augmented_samples = defaultdict(list)
    for idx in tqdm(range(len(samples1))):
        reference = samples1["gpt_oss_references"][idx]

        # print(f"IDX = {idx}")
        reference_dict = ref_to_json(reference, model, config)
        # print(f"Reference Dict = {type(reference_dict)}", flush = True)
        if isinstance(reference_dict, list):
            reference_str = reference_to_str(reference_dict)
        elif isinstance(reference_dict, str):
            reference_str = reference_dict

        feature = None
        if len(samples1["sub_feature"][idx]) > 0: 
            feature = samples1["features"][idx] + "-" + samples1["sub_feature"][idx]
        else:
            feature = samples1["features"][idx]

        testcase = samples2["testcase"][idx]
        testcase = testcase_to_str(testcase)

        augmented_samples["feature"].append(feature)
        augmented_samples["references"].append(reference_str)
        augmented_samples["testcase"].append(testcase)
        augmented_samples["high_level_testcase"].append(samples1['high_level_testcase'][idx])


    augmented_samples = datasets.Dataset.from_dict(augmented_samples)
    augmented_samples.save_to_disk(save_path)