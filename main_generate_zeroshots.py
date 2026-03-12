import datasets
from tqdm import tqdm
from collections import defaultdict
from utils.generate import OClientModelv2, OModelConfig
from datasets import load_from_disk, Dataset


if __name__ == "__main__":

    model_name = "gpt_oss_20b_20k_ctx:latest"
    model_port = "11435"

    model = OClientModelv2(model_name=model_name, port=model_port)
    model_config = OModelConfig(think="low", temperature=0.7)

    dataset_save_path = "Generated_Datasets/zeroshot-baseline.hf"

    test_predictions = defaultdict(list)
    train_predictions = defaultdict(list)

    data = load_from_disk("Datasets/Testcase_Generation_Data")

    prompt = """Given the following feature, test case name, item and references you have to design testcases for it. 
Your test case must have the following sections section title, Test Purpose, Initial Condition, Test Procedure and Expected Outcome.

You must produce your test case in the following format.
### Test Purpose:
<test purpose content>

### Initial Condition:
<initial condition content>

### Test Procedure:
<test procedure content>

### Expected Outcome:
<expected outcome content>

Only output your test case in the above output format with sections mentioned in markdown format and nothing else."""

    train_data = data["train"]
    test_data = data["test"]

    # Process training data
    print("Processing training data...")
    for idx in tqdm(range(len(train_data))):
        reference = train_data[idx]["references"]
        testcase = train_data[idx]["testcase"]
        feature = train_data[idx]["feature"]
        source = train_data[idx]["source"]

        user_prompt = f"""{prompt}

Reference: {reference}

Feature: {feature}"""
        
        model_response = model(prompt=user_prompt, **model_config.__dict__).response

        train_predictions["references"].append(reference)
        train_predictions["testcase"].append(testcase)
        train_predictions["feature"].append(feature)
        train_predictions["source"].append(source)
        train_predictions["generated_testcase"].append(model_response)

    # Process test data
    print("Processing test data...")
    for idx in tqdm(range(len(test_data))):
        reference = test_data[idx]["references"]
        testcase = test_data[idx]["testcase"]
        feature = test_data[idx]["feature"]
        source = test_data[idx]["source"]

        user_prompt = f"""{prompt}

Reference: {reference}

Feature: {feature}"""
        
        model_response = model(prompt=user_prompt, **model_config.__dict__).response

        test_predictions["references"].append(reference)
        test_predictions["testcase"].append(testcase)
        test_predictions["feature"].append(feature)
        test_predictions["source"].append(source)
        test_predictions["generated_testcase"].append(model_response)

    # Create datasets from predictions
    train_dataset = Dataset.from_dict(train_predictions)
    test_dataset = Dataset.from_dict(test_predictions)

    # Combine into DatasetDict
    final_dataset = datasets.DatasetDict({
        "train": train_dataset,
        "test": test_dataset
    })

    # Save the dataset
    print(f"Saving dataset to {dataset_save_path}...")
    final_dataset.save_to_disk(dataset_save_path)
    print("Done!")