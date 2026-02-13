# Prompt-Recovery-by-RL

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


