from utils.build_dataset import MozillaMd
from pathlib import Path
import yaml
import json
from tqdm import tqdm
import time

if __name__ == "__main__":

    with open("Configurations/mozilla_extractions.yaml", "r") as file:
        config = yaml.safe_load(file)

    ### Change the base path accordingly ###

    dir_path = Path(config["output_folder"])
    dir_path.mkdir(parents = True, exist_ok=True)

    mzmd = MozillaMd()

    req_url = config["req_path"]
    tc_url = config["tc_path"]

    req_md = ""
    tc_md = ""

    if config["is_md_make"]:
        
        for r_url in req_url:
            if len(req_md) == 0:
                req_md = mzmd.url_to_md(url = r_url)
            else:
                req_md += "\n\n\n" + mzmd.url_to_md(url = r_url)


        tc_md = mzmd.url_to_md(url = tc_url)

        with open(config["req_md"], "w") as fp:
            fp.write(req_md)

        with open(config["tc_md"], "w") as fp:
            fp.write(tc_md)

    else:
        with open(config["req_md"], "r") as fp:
            req_md = fp.read()

        with open(config["tc_md"], "r") as fp:
            tc_md = fp.read()


    req_json = mzmd.extract_sections(req_md, type_doc=config["doc_type"])

    with open(config["req_json"], "w",  encoding = "utf-8") as fp:
        json.dump(req_json, fp, indent=4, ensure_ascii=False)

    tc_links = mzmd.extract_feature_tc(md=tc_md, type_doc=config["doc_type"])

    with open(config["tc_links"], "w",  encoding = "utf-8") as fp:
        json.dump(tc_links, fp, indent=4, ensure_ascii=False)

    results = []
    for links in tqdm(tc_links):
        time.sleep(0.5)
        if links["tc_name"]:
            link = links["tc_name"]["content"]
            link_md = mzmd.url_to_md(url = link)

            if link_md is not None:
                tc = mzmd.extract_tc(text = link_md)
                
                results.append(
                    {
                        "feature" : links["feature"],
                        "sub_feature" : links["sub_feature"],
                        "description" : links["description"],
                        "tc_name" : links["tc_name"],
                        "test_case" : tc,
                        "reference" : req_json
                    }
                )

    with open(config["tc_json"], "w",  encoding = "utf-8") as fp:
        json.dump(results, fp, indent=4, ensure_ascii=False)

    results = mzmd.make_datasets(results)
    results.save_to_disk(config["hf_dataset_path"])




    







    



