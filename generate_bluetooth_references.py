import datasets
import pickle as pkl
from tqdm import tqdm
import yaml
from collections import defaultdict
import re


def reference_to_str(sample_references):
    output = ""

    for ref_ in sample_references:
        output += ref_[0]["section_title"] + "-\n" + ref_[0]["content"] + "\n\n"

    output = output.strip()
    output = re.sub(r"^Bluetooth SIG Proprietary Page \*\*\d+ of \d+\*\*", "", output, flags=re.MULTILINE | re.IGNORECASE)
    output = re.sub(r"^\*\*Audio/Video Remote Control Profile /\*\* Profile Specification", "", output, flags=re.MULTILINE | re.IGNORECASE)
    output = re.sub(r"^_(Table|Figure).*$", "", output, flags=re.MULTILINE).strip()
    output = re.sub(r'\n+', '\n', output)

    return output.strip() 

def testcase_to_str(testcase):
    output = f"{testcase["section_title"]}\n\n"

    for entry, content in testcase.items():

        if entry == "content":
            for item in content:
                title = item['title']
                content = item['content']

                if title != "Reference":
                    content = re.sub(r"^_Figure.*$", "", content, flags=re.MULTILINE).strip()
                    content = re.sub(r"^\*\*\d+\s*Test case mapping.*$", "", content, flags=re.DOTALL |re.MULTILINE).strip()
                    content = re.sub(r'\n+', '\n', content)
                    output += f"{title}:\n{content}\n\n"

    return output



if __name__ == "__main__":
    with open("Configurations/bluetooth_references_filter.yaml", "r") as file:
        config = yaml.safe_load(file)


    with open(config["dataset_path"], "rb") as fp:
        samples = pkl.load(fp)

    num_samples = len(samples["testcases"])

    augmented_samples = defaultdict(list)

    for idx in tqdm(range(num_samples)):
        if len(samples["testcases"][idx]) > 0 and len(samples["references"][idx]) > 0 and len(samples["feature"][idx]) > 0 and len(samples["item"][idx]) > 0: 
            all_references = samples["references"][idx]

            for test_case_ in samples["testcases"][idx]:
                sample_references = []

                for item_ in test_case_["content"]:
                    if item_["title"] == "Reference" :
                        for ref_id in item_["content"]:
                            for all_ref_ in all_references:
                                if ref_id == all_ref_[0]["section_number"]:
                                    sample_references.append(all_ref_)

                if len(sample_references) > 0:

                    # print(testcase_to_str(test_case_), flush = True)
                    # print(reference_to_str(sample_references))
                    # print("\n\n")

                    augmented_samples["references"].append(reference_to_str(sample_references))
                    augmented_samples["testcase"].append(testcase_to_str(test_case_))
                    augmented_samples["name"].append(test_case_["section_title"])
                    augmented_samples["feature"].append(samples["feature"][idx])
                    augmented_samples["item"].append(samples["item"][idx])


    augmented_samples = datasets.Dataset.from_dict(augmented_samples)
    augmented_samples.save_to_disk(config["output_path"])
    


