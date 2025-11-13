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


class RLAnsDataset(CustomDataset):
    def __init__(self, data_name : str, num_samples : int = 3000):
        self.samples = load_dataset(data_name)["train"]

        self.num_samples = num_samples


    def prepare_dataset(self, base_task_prompt : str, system_prompt : str):
        augmented_samples = defaultdict(list)

        for _ in tqdm(range(self.num_samples)):
            augmented_samples["user_prompt"].append(base_task_prompt)
            augmented_samples["system_prompt"].append(system_prompt)
            augmented_samples["prompt"].append([
                {"role" : "system", "content" : system_prompt},
                {"role" : "user", "content" : base_task_prompt}
            ])

        augmented_samples = datasets.Dataset.from_dict(augmented_samples)
        return augmented_samples


        
