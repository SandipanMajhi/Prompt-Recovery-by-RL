from abc import ABC, abstractmethod
from typing import List, AnyStr, Union
from datasets import load_dataset, load_from_disk, concatenate_datasets
from collections import defaultdict
from tqdm import tqdm
import datasets



class CustomDataset(ABC):
    
    @abstractmethod
    def prepare_dataset(self):
        raise NotImplementedError("Write the Prepare dataset method")
    


####################### Examples ###################################

class PromptOptimDataset(CustomDataset):
    def __init__(self, num_samples : int = 50):
        self.num_samples = num_samples
        self.seed = 42

    def prepare_dataset(self, 
                        data_paths : str,
                        user_prompt : str,
                        system_prompt : str):

        full_dataset = load_from_disk(data_paths)["train"]
        full_dataset = full_dataset.shuffle(seed = self.seed)

        self.num_samples = len(full_dataset)

        augmented_samples = defaultdict(list)
        for idx in tqdm(range(self.num_samples)):

            augmented_samples["user_prompt"].append(user_prompt)
            augmented_samples["system_prompt"].append(system_prompt)

            augmented_samples["reference"].append(full_dataset["references"][idx])
            augmented_samples["feature"].append(full_dataset["feature"][idx])
            augmented_samples["source"].append(full_dataset["source"][idx])
            augmented_samples["specification"].append(full_dataset["requirement_specification"][idx])
            augmented_samples["testcase"].append(full_dataset["testcase"][idx])

            augmented_samples["prompt"].append([
                {"role" : "system", "content" : system_prompt},
                {"role" : "user", "content" : user_prompt}
            ])

        augmented_samples = datasets.Dataset.from_dict(augmented_samples)
        return augmented_samples
    



class RLPRLDataset(CustomDataset):
    def __init__(self, num_samples : int = 3000):
        self.num_samples = num_samples


    def extract_xml_tag(self, text : str, tag : str):
        text = text.split(f"<{tag}>")[-1]
        text = text.split(f"</{tag}>")[0]
        return text.strip()


    def prepare_dataset(self, base_task_prompt : str, system_prompt : str):
        augmented_samples = defaultdict(list)

        input_ = self.extract_xml_tag(text=base_task_prompt, tag="input")
        output_ = self.extract_xml_tag(text = base_task_prompt, tag="output")

        for _ in tqdm(range(self.num_samples)):
            augmented_samples["user_prompt"].append(base_task_prompt)
            augmented_samples["system_prompt"].append(system_prompt)
            augmented_samples["input_instruction"].append(input_)
            augmented_samples["output"].append(output_)
            augmented_samples["prompt"].append([
                {"role" : "system", "content" : system_prompt},
                {"role" : "user", "content" : base_task_prompt}
            ])

        augmented_samples = datasets.Dataset.from_dict(augmented_samples)
        return augmented_samples


        
