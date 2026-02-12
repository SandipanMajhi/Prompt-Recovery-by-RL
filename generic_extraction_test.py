from utils.build_dataset import AVRCPmd, BAPmd, HFPmd, VDPmd
from pathlib import Path
import yaml
import re


if __name__ == "__main__":

    with open("Configurations/generic_extraction.yaml", "r") as file:
        config = yaml.safe_load(file)

    ### Change the base path accordingly ###

    dir_path = Path(config["output_folder"])
    dir_path.mkdir(parents = True, exist_ok=True)

    if config["is_md_make"]:
        AVRCPmd.to_md(pdf_path = config["req_pdf_path"], 
                            output_path=f"{config["output_folder"]}/{config["req_md"]}")
        
        AVRCPmd.to_md(pdf_path = config["tc_pdf_path"], 
                            output_path=f"{config["output_folder"]}/{config["tc_md"]}")


    if config["doc_type"] == "AVRCP":

    
        AVRCPmd.extract_sections(md_path = f"{config["output_folder"]}/{config["req_md"]}",
                                    output_path=f"{config["output_folder"]}/{config["req_json"]}",
                                    granularity = int(config["req_granularity"]))
        
        AVRCPmd.resolve_references(json_path = f"{config["output_folder"]}/{config["req_json"]}",
                                        output_path = f"{config["output_folder"]}/{config["reference_map_name"]}")
        
        AVRCPmd.extract_test_cases(md_path=f"{config["output_folder"]}/{config["tc_md"]}",
                                        output_path = f"{config["output_folder"]}/{config["tc_json"]}")
        
        AVRCPmd.connect_tc_to_req(tc_path = f"{config["output_folder"]}/{config["tc_json"]}",
                                        req_path= f"{config["output_folder"]}/{config["req_json"]}",
                                        output_path = f"{config["output_folder"]}/{config["tc_req_map_name"]}")
        

    if config["doc_type"] == "BAP":

        BAPmd.extract_sections(md_path = f"{config["output_folder"]}/{config["req_md"]}",
                                    output_path=f"{config["output_folder"]}/{config["req_json"]}",
                                    granularity = int(config["req_granularity"]))
        
        BAPmd.resolve_references(json_path = f"{config["output_folder"]}/{config["req_json"]}",
                                        output_path = f"{config["output_folder"]}/{config["reference_map_name"]}")
        
        BAPmd.extract_test_cases(md_path=f"{config["output_folder"]}/{config["tc_md"]}",
                                        output_path = f"{config["output_folder"]}/{config["tc_json"]}")
        
        BAPmd.connect_tc_to_req(tc_path = f"{config["output_folder"]}/{config["tc_json"]}",
                                        req_path= f"{config["output_folder"]}/{config["req_json"]}",
                                        output_path = f"{config["output_folder"]}/{config["tc_req_map_name"]}")
        

    if config["doc_type"] == "HFP":

        HFPmd.extract_sections(md_path = f"{config["output_folder"]}/{config["req_md"]}",
                                    output_path=f"{config["output_folder"]}/{config["req_json"]}",
                                    granularity = int(config["req_granularity"]))
        
        HFPmd.resolve_references(json_path = f"{config["output_folder"]}/{config["req_json"]}",
                                        output_path = f"{config["output_folder"]}/{config["reference_map_name"]}")
        
        HFPmd.extract_test_cases(md_path=f"{config["output_folder"]}/{config["tc_md"]}",
                                        output_path = f"{config["output_folder"]}/{config["tc_json"]}")
        
        HFPmd.connect_tc_to_req(tc_path = f"{config["output_folder"]}/{config["tc_json"]}",
                                        req_path= f"{config["output_folder"]}/{config["req_json"]}",
                                        output_path = f"{config["output_folder"]}/{config["tc_req_map_name"]}")
        

    if config["doc_type"] == "VDP":

        HFPmd.extract_sections(md_path = f"{config["output_folder"]}/{config["req_md"]}",
                                    output_path=f"{config["output_folder"]}/{config["req_json"]}",
                                    granularity = int(config["req_granularity"]))
        
        HFPmd.resolve_references(json_path = f"{config["output_folder"]}/{config["req_json"]}",
                                        output_path = f"{config["output_folder"]}/{config["reference_map_name"]}")
        
        VDPmd.extract_test_cases(md_path=f"{config["output_folder"]}/{config["tc_md"]}",
                                        output_path = f"{config["output_folder"]}/{config["tc_json"]}")
        
        HFPmd.connect_tc_to_req(tc_path = f"{config["output_folder"]}/{config["tc_json"]}",
                                        req_path= f"{config["output_folder"]}/{config["req_json"]}",
                                        output_path = f"{config["output_folder"]}/{config["tc_req_map_name"]}")
