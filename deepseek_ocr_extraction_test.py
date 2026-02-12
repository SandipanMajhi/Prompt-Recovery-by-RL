from utils.build_dataset import PDFtoMarkDown
from utils.build_dataset import DeepSeekmdProcess
from utils.deepseek_ocr_generate import ocr_model
from utils.generate import OClientModel, OModelConfig
from pathlib import Path
import yaml
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--config", type = str, default = "Configurations/deepseek_ocr_extraction.yaml")
    args = parser.parse_args()

    with open(args.config, "r") as file:
        config = yaml.safe_load(file)

    ### Change the base path accordingly ###

    dir_path = Path(config["output_folder"])
    dir_path.mkdir(parents = True, exist_ok=True)

    if config["is_md_make"]:

        model = ocr_model()

        # DeepSeekmdProcess.images_to_md(model = model,
        #                                image_folder=config["req_img_folder"],
        #                                output_path = config["req_md"],
        #                                )

        DeepSeekmdProcess.images_to_md(model = model,
                                       image_folder=config["tc_img_folder"],
                                       output_path = config["tc_md"],
                                       output_dir_path=config["tc_md_parent_dir"])
        

    # if config["is_md_clean"]:

    #     DeepSeekmdProcess.clean_md(md_path=config["req_md"],
    #                                output_path=config["clean_req_md"])
        
    #     DeepSeekmdProcess.clean_md(md_path = config["tc_md"],
    #                                output_path = config["clean_tc_md"])
        
    # #### Building the dataset ####
    
    # DeepSeekmdProcess.extract_sections(md_path = config["clean_req_md"],
    #                                    output_path= config["req_json"],
    #                                    granularity=config["granularity"])
    
    
    # DeepSeekmdProcess.resolve_references(json_path=config["req_json"],
    #                                      output_path = config["req_references"])
    

    # # PDFtoMarkDown.extract_test_cases(md_path=config["tc_extraction_md"],
    # #                                  output_path=config["tc_json"])

    # DeepSeekmdProcess.extract_test_cases(md_path = config["clean_tc_md"],
    #                                      output_path=config["tc_json"])

    DeepSeekmdProcess.connect_tc_to_req(tc_path="Datasets/Generic_Extractions/tc.json",
                                        req_path="Datasets/DeepSeek_Extractions/Deepseek_Extractions_doc_1/req.json",
                                        ref_path="Datasets/DeepSeek_Extractions/Deepseek_Extractions_doc_1/req_references.json",
                                        output_path="Datasets/DeepSeek_Extractions/Deepseek_Extractions_doc_1/tc_req.json"
                                    )



    


        

    
    