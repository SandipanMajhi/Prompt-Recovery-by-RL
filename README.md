# Prompt-Recovery-by-RL

## Generation Workflow 

Inputs : Features, Sub Features, References, Item, High Level Test Case (May be ignore this)  
Output : Full Length Test Case

## Requirements
You might want to delete some packages from the list if it is not needed.
```
  pickle
  torch
  numpy
  matplotlib
  scikit-learn
  transformers
  xformers
  datasets
  peft
  pandas
  rouge_score
  evaluate
  nltk
  stanza
  accelerate
  bitsandbytes
  bert-score
  sentence-transformers
  trl
  vllm
  unsloth
```

## Dataset USage

## Bluetooth

### File paths: 

```
  AVRCP : Datasets/Generic_Extractions/AVRCP/bluetooth_1.pkl
  BAP: Datasets/Generic_Extractions/BAP/bluetooth_2.pkl
  HFP: Datasets/Generic_Extractions/HFP/bluetooth_3.pkl  
  VDP: Datasets/Generic_Extractions/VDP/bluetooth_4.pkl 
```

#### HF files: (152 test Cases)

```
  AVRCP: Datasets/Generic_Extractions/AVRCP/bluetooth_1.hf
  BAP: Datasets/Generic_Extractions/BAP/bluetooth_2.hf
  HFP: Datasets/Generic_Extractions/HFP/bluetooth_3.hf
```

### Dataset Description: 

```
  Columns: references, testcases, item, feature, test_cases_ids
```

### How to import and use:

```
  import pickle as pkl

  with open(data_path, "rb") as fp:
    data = pkl.load(fp)

  #### Check columns ###
  print(list(data.keys()))

  ### Access data at id = 0 ###
  current_testcase = data["testcases"][0]
  ....
```

Load HF Files:

```
  from datasets import load_from_disk
  samples = load_from_disk(hf_path)
```

### Column Description and probable usage:

```
  'references' : Text from Requirement Document [Input]
  'testcases' : Original Full length test cases for the feature [Output]
  'item' : Item ID [Input]
  'feature' : Feature Name [Input]
  'test_cases_ids' : Original TestCase ID [Probably Output]
```

#### Columns in HF files: (Explanations just like before)

You can use `name` as input
```
  'references', 'testcase', 'name', 'feature', 'item'
```

## Mozilla TestCases

### File Paths:

#### Original Test Cases extracted from Mozilla Archive.

```
  Mozilla_R1: Datasets/Generic_Extractions/Mozilla_R1/Mozilla_R1.hf
  Mozilla_R2: Datasets/Generic_Extractions/Mozilla_R2/Mozilla_R2.hf
  Mozilla_R3: Datasets/Generic_Extractions/Mozilla_R3/Mozilla_R3.hf
  Mozilla_R4: Datasets/Generic_Extractions/Mozilla_R4/Mozilla_R4.hf
```

#### GPT-OSS-20B references top-3 attached Mozilla Test Cases

```
  Mozilla_R1: Datasets/Generic_Extractions/Mozilla_R1/Mozilla_R1_GPT_OSS_20b_references.hf
  Mozilla_R2: Datasets/Generic_Extractions/Mozilla_R2/Mozilla_R2_GPT_OSS_20b_references.hf
  Mozilla_R3: Datasets/Generic_Extractions/Mozilla_R3/Mozilla_R3_GPT_OSS_20b_references.hf
  Mozilla_R4: Datasets/Generic_Extractions/Mozilla_R4/Mozilla_R4_GPT_OSS_20b_references.hf
```

### How to import and use

```
  from datasets import load_from_disk

  samples = load_from_disk("Datasets/Generic_Extractions/Mozilla_R1/Mozilla_R1_GPT_OSS_20b_references.hf")
```

### Column Description and probable usage:

```
  'features': Main name of the feature [Input]
  'sub_feature': Sub feature name [Input] (Sometimes empty)
  'high_level_testcase': High level testcase description [Output probably] 
  'reference': Full Reference document (Almost 16k tokens) [Input]
  'gpt_oss_references': GPT-OSS-20B generated top-3 sections from the reference doc
```





