from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from accelerate import init_empty_weights, infer_auto_device_map
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModel
from peft import LoraConfig, TaskType, get_peft_model, PeftModelForCausalLM
from dataclasses import dataclass
from transformers import BitsAndBytesConfig, set_seed
import torch
import requests
import re
import ollama
from ollama import chat
from typing import Union
import os
import json




quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16
) 

@dataclass
class OModelConfig:
    temperature : float = 0.0
    top_p : float = 0.9
    seed : int = 42
    think : str = False

@dataclass
class HModelConfig:
    temperature : float = 0.01
    top_p : float = 0.9
    min_p : float = 0.1
    max_new_tokens : int = 256
    seed : int = 42

@dataclass
class VLLMConfig:
    temperature : float = 0.01
    top_p : float = 0.9
    min_p : float = 0.1
    max_tokens : int = 256
    seed : int = 42


@dataclass
class ResponseBase:
    response : str = ""
        


class EmbeddingModel_Ollama:
    def __init__(self, model_name = "nomic-embed-text:latest"):
        self.model_name = model_name

    def __call__(self, text : str):
        return ollama.embed(model=self.model_name, input=[text])
    
    def batched_embed(self, texts : List[str]):
        return ollama.embed(model = self.model_name, input=texts)
    

class EmbeddingModel_Huggingface:
    def __init__(self, device = "cpu"):
        self.model_name = "NovaSearch/stella_en_400M_v5"
        self.query_prompt_name = "s2p_query"

        if device.startswith("cuda"):
            print(f"Using Device = {device}")
            self.model = SentenceTransformer("dunzhang/stella_en_400M_v5", trust_remote_code=True).to(device=device)
        else:
            self.model = SentenceTransformer(
                        "dunzhang/stella_en_400M_v5",
                        trust_remote_code=True,
                        device="cpu",
                        config_kwargs={"use_memory_efficient_attention": False, "unpad_inputs": False}
                    )


    def __repr__(self):
        return f"Embedding model with {self.model_name}"

    def similarity_embed(self, queries : List[str], docs : List[str]):
        query_embeddings = self.model.encode(queries, prompt_name=self.query_prompt_name)
        doc_embeddings = self.model.encode(docs)
        similarities = self.model.similarity(query_embeddings, doc_embeddings)

        return similarities
    
    def get_embedding(self, queries : List[str]):
        query_embeddings = self.model.encode(queries)
        return query_embeddings



class OModel:
    def __init__(self, model_name="llama3.1"):
        self.model_name = model_name

    def __call__(self, prompt):
        return ollama.generate(model=self.model_name, prompt=prompt)
    

class OClientModelv2:
    def __init__(self, model_name : str, port : str):
        self.model_name = model_name
    
    def __call__(self, prompt : str, **kwargs):
        response = chat(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            options={
                "temperature": kwargs["temperature"],
                "top_p" : kwargs["top_p"],
                "seed" : kwargs["seed"]
            },
            think= kwargs["think"]
        )

        return ResponseBase(response=response["message"]["content"])
    

class OClientModel:
    def __init__(self, model_name="llama3.1", port = "8080", seed = 42):
        self.model_name = model_name
        self.client = ollama.Client(
        host=f'http://localhost:{port}',
        headers={'x-some-header': 'some-value'}
        )

        self.seed = seed

    def __call__(self, prompt : str, **kwargs):

        system_prompt = ''

        if "system_prompt" in kwargs:
            system_prompt = kwargs["system_prompt"]

        if "temperature" in kwargs:
            temperature = float(kwargs["temperature"])
        else:
            temperature = None

        if "top_p" in kwargs:
            top_p = float(kwargs["top_p"])
        else:
            top_p = None

        if "seed" in kwargs:
            self.seed = int(kwargs["seed"])
        

        if top_p is None and temperature is None:
            response = self.client.generate(model=self.model_name, prompt=prompt, system=system_prompt)
        
        if top_p is None and temperature is not None:
            response = self.client.generate(model = self.model_name, 
                                            prompt=prompt, 
                                            options= {"temperature" : temperature,
                                                      "seed" : self.seed}, system=system_prompt)
            
        if top_p is not None and temperature is None:
            response = self.client.generate(model = self.model_name, 
                                            prompt=prompt, 
                                            options= {"top_p" : top_p,
                                                      "seed": self.seed}, system=system_prompt)
            
        if top_p is not None and temperature is not None:
            response = self.client.generate(model = self.model_name, 
                                            prompt=prompt, 
                                            options= {"top_p" : top_p,
                                                      "temperature" : temperature,
                                                      "seed" : self.seed
                                                    }
                                            , system=system_prompt)

        if "deepseek" in self.model_name:
            response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL).strip()
            response = ResponseBase(response = response)

        return response
    

class HCLientModel:
    def __init__(self, model_name : str, 
                 quantized : bool = True):
        
        self.model_name = model_name

        if quantized:
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )

            self.h_model = AutoModelForCausalLM.from_pretrained(
                model_name,
                device_map = "auto",
                quantization_config = bnb_config
            )
        
        else:

            self.h_model = AutoModelForCausalLM.from_pretrained(
                model_name,
                device_map = "auto"
            )

        self.h_tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            use_fast = True,
            padding = True
        )

        if self.h_tokenizer.pad_token is None or self.h_model.config.pad_token_id is None:
            self.h_tokenizer.pad_token = self.h_tokenizer.eos_token
            self.h_tokenizer_pad_token_id = self.h_tokenizer.eos_token_id
            self.h_model.config.pad_token_id = self.h_model.config.eos_token_id

        self.h_model.eval()

    
    def __call__(self, 
                 prompt : str, 
                 config : Union[OModelConfig, HModelConfig] = None,
                 system_prompt : str = None):

        if config is None:
            config = HModelConfig()


        if "Instruct" in self.model_name:
            if system_prompt is None:
                system_prompt = "You are an helpful assistant who helps in solving a task according to given instruction."

            prompt_ = [
                    {"role" : "system", "content" : system_prompt},
                    {"role" : "user", "content" : prompt}
                ]

            inputs = self.h_tokenizer.apply_chat_template(prompt_, return_tensors="pt").to(self.h_model.device)
            # decoded_string = self.h_tokenizer.decode(inputs[0], skip_special_tokens=False)
            # print(f"your prompt = {decoded_string}", flush = True)

            input_len = inputs.shape[1]
            set_seed(config.seed)
            output = self.h_model.generate(inputs, 
                                        do_sample = True,
                                        temperature = config.temperature,
                                        top_p = config.top_p,
                                        min_p = config.min_p,
                                        max_new_tokens = config.max_new_tokens,
                                        pad_token_id=self.h_tokenizer.pad_token_id)
            
            output = output[0, input_len:]
            output = self.h_tokenizer.decode(output, skip_special_tokens = True)
            output = output.replace("assistant\n\n","")
            output = output.strip()
            output = ResponseBase(response = output)
        
        else:
            inputs = self.h_tokenizer([prompt], return_tensors = "pt").to(self.h_model.device)
            input_len = inputs.input_ids.shape[1]
            set_seed(config.seed)
            
            output = self.h_model.generate(**inputs, 
                                        do_sample = True,
                                        temperature = config.temperature,
                                        top_p = config.top_p,
                                        min_p = config.min_p,
                                        max_new_tokens = config.max_new_tokens,
                                        pad_token_id=self.h_tokenizer.pad_token_id)
            
            output = output[0, input_len:]
            output = self.h_tokenizer.decode(output, skip_special_tokens = True)
            output = output.replace("assistant\n\n","")
            output = output.strip()
            output = ResponseBase(response = output)
        
        return output

class OCR:
    def __init__(self, model_name : str = "deepseek-ai/DeepSeek-OCR"):
        self.model_name = model_name

        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(model_name, 
                                               _attn_implementation='eager',
                                               trust_remote_code=True, 
                                               use_safetensors=True)
        
        self.model = self.model.eval().cuda().to(torch.bfloat16)


    def __call__(self, image_path : str, output_dir : str):
        prompt = f""""{image_path}" Convert the document to markdown."""
        
        # infer(self, tokenizer, prompt='', image_file='', output_path = ' ', base_size = 1024, image_size = 640, crop_mode = True, test_compress = False, save_results = False):

        # Tiny: base_size = 512, image_size = 512, crop_mode = False
        # Small: base_size = 640, image_size = 640, crop_mode = False
        # Base: base_size = 1024, image_size = 1024, crop_mode = False
        # Large: base_size = 1280, image_size = 1280, crop_mode = False

        # Gundam: base_size = 1024, image_size = 640, crop_mode = True

        res = self.model.infer(self.tokenizer, 
                               prompt=prompt, 
                               image_file=image_path, 
                               output_path = output_dir, 
                               base_size = 1024, 
                               image_size = 640, 
                               crop_mode=True, 
                               save_results = True, 
                               test_compress = True)
            

class deepseek_ocr:
    def __init__(self, port : str):
        self.port = port


    def __call__(self, image_path : str, instruction : str):
        url = f"http://localhost:{self.port}/api/generate"
        data = {
            "model": "deepseek-ocr:3b",
            "prompt": f'{image_path} {instruction}',
            "stream": True
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            print(response.json()['response'])
        else:
            print(f"Error: {response.status_code}, {response.text}")