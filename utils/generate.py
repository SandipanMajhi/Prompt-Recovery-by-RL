from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from accelerate import init_empty_weights, infer_auto_device_map
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig, pipeline
from peft import LoraConfig, TaskType, get_peft_model, PeftModelForCausalLM
from dataclasses import dataclass
from transformers import BitsAndBytesConfig, set_seed
import torch
import requests
import re
import ollama
from typing import Union
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest


quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16
) 

@dataclass
class OModelConfig:
    temperature : float = 0.0
    top_p : float = 0.9
    seed : int = 42

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
    

class OClientModel:
    def __init__(self, model_name="llama3.1", port = "8080", seed = 42):
        self.model_name = model_name
        self.client = ollama.Client(
        host=f'http://localhost:{port}',
        headers={'x-some-header': 'some-value'}
        )

        self.seed = seed

    def __call__(self, prompt : str, **kwargs):
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
            response = self.client.generate(model=self.model_name, prompt=prompt)
        
        if top_p is None and temperature is not None:
            response = self.client.generate(model = self.model_name, 
                                            prompt=prompt, 
                                            options= {"temperature" : temperature,
                                                      "seed" : self.seed})
            
        if top_p is not None and temperature is None:
            response = self.client.generate(model = self.model_name, 
                                            prompt=prompt, 
                                            options= {"top_p" : top_p,
                                                      "seed": self.seed})
            
        if top_p is not None and temperature is not None:
            response = self.client.generate(model = self.model_name, 
                                            prompt=prompt, 
                                            options= {"top_p" : top_p,
                                                      "temperature" : temperature,
                                                      "seed" : self.seed
                                                    }
                                            )

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



class VLLMClient:
    def __init__(self, model_name: str, lora_path: str = None):
        # Pass the lora_path directly to the LLM constructor
        self.llm = LLM(
            model=model_name,
            enable_lora=True,
            max_loras=1, # Number of LoRAs that can be loaded simultaneously
            max_lora_rank=64, # Maximum LoRA rank (usually 64 or 128)
            trust_remote_code=True,
            quantization="bitsandbytes"
        )
        self.lora_path = lora_path

    def __call__(self, prompt: str, config):
        # Create a LoRARequest object to specify the adapter to use for this request.
        lora_request = LoRARequest(
            lora_path=self.lora_path,
            lora_name="QGen_adapter", # A name to identify the adapter
            lora_int_id=1
        )

        system_prompt = "You are an helpful assistant who helps in solving a task according to given instruction."

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        tokenizer = self.llm.get_tokenizer(lora_request=lora_request)
        
        # Use the tokenizer to apply the model's specific chat template.
        # This converts the list of dictionaries into a single string.
        formatted_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        

        sampling_params = SamplingParams(**config.__dict__)

        # Pass the lora_request to the generate method.
        outputs = self.llm.generate(
            prompts=formatted_prompt,
            sampling_params=sampling_params,
            lora_request=lora_request
        )

        return outputs