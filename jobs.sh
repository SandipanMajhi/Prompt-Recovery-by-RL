CUDA_VISIBLE_DEVICES=1 nohup python main_runner.py \
    --ollama_model llama3.1:8b \
    --port 11434 \
    --policy_model_name meta-llama/Llama-3.1-8B-Instruct \
    --saved_model_name Models/prl_model_500_v2.mdl \
    --num_train_samples 3000 \
    --train_steps 500 \
    --max_prompt_len 4196 \
    --max_seq_len 16000 \
    --output_dir Outputs/prl_model_500_v2 \
    --beta 0.01 \
    > prl_test.log &

CUDA_VISIBLE_DEVICES=1 nohup python main_inference.py \
    --policy_model_name meta-llama/Llama-3.1-8B-Instruct \
    --lora_adapter_path Models/prl_model_500.mdl \
    --ollama_model_name llama3.1:8b \
    --port 11434 \
    > prompt_optim_comp.log &


CUDA_VISIBLE_DEVICES=1 nohup python test_deepseek_ocr.py \
    > deepseek.log &


nohup python test.py \
    > markdown_text.log &

#### RUN OCR Extraction ####
CUDA_VISIBLE_DEVICES=0 nohup yes y | python deepseek_ocr_extraction_test.py > output.log 2>&1 &


#### Now build json ####
nohup python deepseek_ocr_extraction_test.py \
    --config Configurations/deepseek_ocr_extraction.yaml \
    > test.log &



#### Build up mozilla references ###
nohup python generate_mozilla_references.py > mozilla_1_builder.log &

