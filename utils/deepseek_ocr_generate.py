from unsloth import FastVisionModel
import torch
from contextlib import redirect_stdout
from transformers import AutoModel
import os
import io
os.environ["UNSLOTH_WARN_UNINITIALIZED"] = '0'

from huggingface_hub import snapshot_download
# snapshot_download("unsloth/DeepSeek-OCR", local_dir = "deepseek_ocr")


class ocr_model:
    def __init__(self):
        self.model, self.tokenizer = FastVisionModel.from_pretrained(
            "unsloth/DeepSeek-OCR",
            load_in_4bit = False,
            auto_model = AutoModel,
            trust_remote_code = True,
            unsloth_force_compile = True,
            use_gradient_checkpointing = "unsloth",
        )

    def __call__(self, image_path : str, output_dir : str):
        # prompt = "<image>\nFree OCR. "
        prompt = "<image>\n<|grounding|>Convert the document to markdown. "
        image_file = image_path
        output_path = output_dir
        fp = io.StringIO()
        with redirect_stdout(fp):
            self.model.infer(self.tokenizer, 
                               prompt=prompt, 
                               image_file=image_file, 
                               output_path = output_path, 
                               base_size = 1024, 
                               image_size = 640, 
                               crop_mode=True, 
                               save_results = False, 
                               test_compress = False)
        
        res = fp.getvalue().strip()
        return res
        
        
        

class pdf_ocr:
    def __init__(self, pdf_path : str):
        pass