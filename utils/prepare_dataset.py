from abc import ABC, abstractmethod
from datasets import load_dataset, load_from_disk
from collections import defaultdict
from tqdm import tqdm
import datasets



class CustomDataset(ABC):
    
    @abstractmethod
    def prepare_dataset(self):
        raise NotImplementedError("Write the Prepare dataset method")
    


####################### Examples ###################################


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


        
