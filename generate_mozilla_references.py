import datasets
from datasets import load_from_disk
from tqdm import tqdm
from utils.build_dataset import MozillaReferences
import yaml
from pathlib import Path


if __name__ == "__main__":

    with open("Configurations/mozilla_build_ref_config.yaml", "r") as file:
        config = yaml.safe_load(file)

    ### Change the base path accordingly ###

    dir_path = Path(config["output_folder"])
    dir_path.mkdir(parents = True, exist_ok=True)

    moz_ref = MozillaReferences(model_name = config["ollama_model_name"], port = config["ollama_port"], think_effort=config["think"])

    moz_ref.build_refs(data_path=config["hf_dataset_path"],
                       save_path=config["hf_dataset_new_path"],
                       num_trials=config["num_trials"])
    






