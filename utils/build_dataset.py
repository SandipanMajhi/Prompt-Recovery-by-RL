# from utils.deepseek_ocr_generate import ocr_model
import os
import glob
import pymupdf4llm
import json
import re
from tqdm import tqdm
from collections import defaultdict
from typing import List, Dict
import html2text
import requests
import evaluate
import datasets




# class DeepSeekmdProcess:

#     @classmethod
#     def images_to_md(cls,
#                      model, 
#                      image_folder : str, 
#                      output_path : str,
#                      output_dir_path : str):
        
#         all_images = glob.glob(f"{image_folder}/*")
#         all_images.sort()

#         all_markdowns = {}

#         output_dir = "/".join(output_path.split("/")[:-1])

#         for img_ in tqdm(all_images):
#             result = model(image_path=img_,
#                         output_dir=output_dir_path)
            
#             img_ = int(img_.split("/")[-1].split(".")[0])
#             all_markdowns[img_] = result

#         all_markdowns = sorted(all_markdowns.items(), key = lambda x : x[0])
        
#         all_markdowns = [md_[1] for md_ in all_markdowns]

#         with open(output_path, "w") as fp:
#             fp.writelines(all_markdowns)
#             fp.close()

#     @classmethod 
#     def clean_md(cls, md_path : str, output_path : str):
#         with open(md_path, "r") as fp:
#             md_data = fp.read()

#         pattern = r"=====================\nBASE:  torch\.Size\(\[1, 256, 1280\]\)\nPATCHES:  torch\.Size\(\[6, 100, 1280\]\)\n====================="
#         md_data = re.sub(pattern, "\n", md_data)

#         hash_pattern = r"(?m)^#+\s+(?=\d)"
#         md_data = re.sub(hash_pattern, "", md_data)

#         bold_title_pattern = r"(?m)^\*\*(.*?)\*\*"
#         md_data = re.sub(bold_title_pattern, r"\1", md_data)

#         with open(output_path, "w") as fp:
#             fp.write(md_data)


#     @classmethod
#     def extract_sections(cls, 
#                          md_path : str, 
#                          output_path : str,
#                          granularity : int = 3):
        
#         with open(md_path, "r") as fp:
#             md_data = fp.read()

#         json_out = []
#         for gran_ in range(2, granularity + 1):
#             prefix = r"\d+" + (r"\.\d+" * (gran_ - 1))
#             lookahead_any_gran = r"\d+(?:\.\d+)*"


#             if gran_ >= 3:
#                 pattern = (
#                     r"(?P<num>" + prefix + r")\s+(?P<title>.*?)\n"
#                     r"(?P<text>[\s\S]*?)"
#                     r"(?=\n" + lookahead_any_gran + r"|$)"
#                 )

#             else:
#                 pattern = (
#                     r"(?P<num>" + prefix + r")\s+(?P<title>.*?)\n"
#                     r"(?P<text>[\s\S]*?)"
#                     r"(?=\n" + prefix + r"|$)"
#                 )

#             matches = re.finditer(pattern, md_data)

#             for match in tqdm(list(matches)):
#                 section_num = match.group('num').strip()
#                 section_title = match.group('title').strip()
#                 text = match.group('text')

#                 clean_text = re.sub(r"Bluetooth SIG Proprietary Page \d+ of \d+", "", text)
#                 clean_text = re.sub(r"Audio/Video Remote Control Profile / Profile Specification", "", clean_text)
                
#                 clean_text = re.sub(r"_Figure \d+\.\d+.*_", "", clean_text)
                
#                 clean_text = clean_text.strip()

#                 json_out.append({
#                     "section_number": section_num,
#                     "section_title": section_title,
#                     "content": clean_text
#                 })

#         with open(output_path, "w", encoding="utf-8") as fp:
#             json.dump(json_out, fp, indent = 4, ensure_ascii=False)


#     @classmethod
#     def resolve_references(cls, 
#                            json_path : str,
#                            output_path : str):
        
#         with open(json_path, "r") as fp:
#             json_out = json.load(fp)

#         pattern = r"(\d+(?:\.\d+)+)"
#         references_adj_list = defaultdict(list)

#         all_keys = [section["section_number"] for section in json_out]

#         for section in json_out:
#             section_num = section["section_number"]
#             section_content = section["content"]
#             matches = re.findall(pattern, section_content)

#             for reference in matches:
#                 references_adj_list[section_num].append(reference)


#         for key1 in all_keys:
#             for key2 in all_keys:
#                 if key1 != key2:
#                     if key1 in key2:
#                         references_adj_list[key1].append(key2)


#         with open(output_path, "w", encoding="utf-8") as fp:
#             json.dump(references_adj_list, fp, indent=4, ensure_ascii=False)


#     @classmethod
#     def extract_test_cases(cls,
#                             model,
#                             md_path: str,
#                             output_path: str):
        
#         prompt = ""
        
#         with open(md_path, "r", encoding="utf-8") as fp:
#             md_data = fp.read()

#         pattern = "=====================\nBASE:  torch.Size([1, 256, 1280])\nPATCHES:  torch.Size([6, 100, 1280])\n====================="
#         md_data = md_data.split(pattern)
#         extracted_testcases = []

#         for md_page in tqdm(md_data):
#             pass

#     @classmethod
#     def connect_tc_to_req(cls, tc_path : str, ref_path : str, req_path : str, output_path : str):
#         with open(tc_path, "r", encoding="utf-8") as fp:
#             test_cases = json.load(fp)

#         with open(req_path, "r", encoding = "utf-8") as fp:
#             req = json.load(fp)

#         with open(ref_path, "r", encoding="utf-8") as fp:
#             ref_json = json.load(fp)

#         tc_req_mapper = defaultdict(list)

#         for case in tqdm(test_cases):
#             section_id = case["section_id"]
#             references = case["content"][1]["content"]

#             for ref in references:
#                 for requirement in req:
#                     req_num = requirement["section_number"]
#                     if ref == req_num:
#                         tc_req_mapper[section_id].append(requirement)


#         with open(output_path, "w", encoding="utf-8") as fp:
#             json.dump(tc_req_mapper, fp, indent = 4)





class AVRCPmd:
    @classmethod
    def to_md(cls, pdf_path : str, output_path : str):
        md_text = pymupdf4llm.to_markdown(pdf_path)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_text)

    @classmethod
    def tc_mapping_read(cls, tc_map_md : str):
        pattern = r"^\s*\|?\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|?\s*$"
        results = []

        for line in tc_map_md.strip().split('\n'):
            if re.match(r"^\s*\|?[\s\-|]+\|?\s*$", line):
                continue
                
            match = re.search(pattern, line)
            if match:
                item = match.group(1).strip()
                feature = match.group(2).strip()
                test_cases_raw = match.group(3).strip()

                if item.lower() == "item":
                    continue

                test_cases = [tc.strip() for tc in test_cases_raw.split('<br>')]

                results.append({
                    "item": item.replace('<br>', '\n'), # Clean up internal breaks
                    "feature": feature.replace('<br>', '\n'),
                    "test_cases": test_cases
                })

        return results


    @classmethod
    def _add_children(cls, 
                      reference_file : str,  
                      requirements : List[Dict]):
        
        with open(reference_file, "r", encoding="utf-8") as fp:
            references = json.load(fp)

        req_dict = {req["section_number"] for req in requirements}

        ### To be edited later ##


    @classmethod
    def connect_tc_to_req(cls, tc_path : str, req_path : str, output_path : str):
        with open(tc_path, "r", encoding="utf-8") as fp:
            test_cases = json.load(fp)

        with open(req_path, "r", encoding = "utf-8") as fp:
            req = json.load(fp)

        tc_req_mapper = defaultdict(list)

        for case in tqdm(test_cases):
            section_id = case["section_id"]
            references = case["content"][1]["content"]

            for ref in references:
                for requirement in req:
                    req_num = requirement["section_number"]
                    if ref == req_num:
                        tc_req_mapper[section_id].append(requirement)


        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(tc_req_mapper, fp, indent = 4)


    @classmethod
    def extract_test_cases(cls, md_path : str, output_path : str, pattern : str = None):
        with open(md_path, "r", encoding="utf-8") as fp:
            sample_text = fp.read()

        
        pattern = r"\*\*(AVRCP\/.*?)\s+\[(.*?)\]\*\*(.*?)(?=\*\*AVRCP\/|\*\*\d+\.[\d\.]*|$)"
        sub_pattern = r"-\s*(.*?)\n\n+(.*?)(?=\n-\s*|\*\*\d+\.[\d\.]*|$)"
        reference_pattern = r"\b\d+(?:\.\d+){2,}\b"

        matches = re.finditer(pattern, sample_text, re.DOTALL)

        all_test_cases = []

        for match in matches:
            section_id = match.group(1).strip()
            section_title = match.group(2).strip()
            content = match.group(3).strip()
    
            cleaned_content = re.sub(r"Bluetooth SIG Proprietary.*?Test Suite", "", content, flags=re.DOTALL)

            sub_matches = re.findall(sub_pattern, cleaned_content, re.DOTALL)

            parsed_data = []
            for title, content in sub_matches:
                # Clean up extra whitespace and newlines
                clean_title = title.strip()
                clean_content = content.strip()

                if clean_title == "Reference":
                    ref_matches = re.finditer(reference_pattern, clean_content)
                    clean_content = [match.group() for match in ref_matches]

                parsed_data.append({
                    "title" : clean_title,
                    "content" : clean_content
                })

            all_test_cases.append({
                "section_id" : section_id,
                "section_title" : section_title,
                "content" : parsed_data
            })

        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(all_test_cases, fp, indent=4, ensure_ascii=False)

            

    @classmethod
    def extract_sections(cls, 
                         md_path: str, 
                         output_path: str, 
                         granularity : int = 3):
        with open(md_path, "r", encoding="utf-8") as fp:
            sample_text = fp.read()

        json_out = []

        for gran_ in range(2, granularity + 1):
            prefix = r"\d+" + (r"\.\d+" * (gran_ - 1))
            lookahead_any_gran = r"\d+(?:\.\d+)*"


            if gran_ >= 3:
                pattern = (
                    r"\*\*(?P<num>" + prefix + r")\*\*\s+\*\*(?P<title>.*?)\*\*\n"
                    r"(?P<text>[\s\S]*?)"
                    r"(?=\n\*\*" + lookahead_any_gran + r"\*\*|$)"
                )

            else:
                pattern = (
                    r"\*\*(?P<num>" + prefix + r")\*\*\s+\*\*(?P<title>.*?)\*\*\n"
                    r"(?P<text>[\s\S]*?)"
                    r"(?=\n\*\*" + prefix + r"\*\*|$)"
                )

            matches = re.finditer(pattern, sample_text)

            for match in tqdm(list(matches)):
                section_num = match.group('num').strip()
                section_title = match.group('title').strip()
                text = match.group('text')

                clean_text = re.sub(r"Bluetooth SIG Proprietary Page \d+ of \d+", "", text)
                clean_text = re.sub(r"Audio/Video Remote Control Profile / Profile Specification", "", clean_text)
                
                clean_text = re.sub(r"_Figure \d+\.\d+.*_", "", clean_text)
                
                clean_text = clean_text.strip()

                json_out.append({
                    "section_number": section_num,
                    "section_title": section_title,
                    "content": clean_text
                })

        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(json_out, fp, indent=4, ensure_ascii=False)
    
    @classmethod
    def resolve_references(cls, 
                           json_path : str, 
                           output_path : str):
        
        with open(json_path, "r") as fp:
            json_out = json.load(fp)

        pattern = r"(\d+(?:\.\d+)+)"
        references_adj_list = defaultdict(list)

        all_keys = [section["section_number"] for section in json_out]

        for section in json_out:
            section_num = section["section_number"]
            section_content = section["content"]
            matches = re.findall(pattern, section_content)

            for reference in matches:
                references_adj_list[section_num].append(reference)


        for key1 in all_keys:
            for key2 in all_keys:
                if key1 != key2:
                    if key1 in key2:
                        references_adj_list[key1].append(key2)


        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(references_adj_list, fp, indent=4, ensure_ascii=False)


    @classmethod
    def tc_section_mapper(cls):
        pass



class BAPmd(AVRCPmd):

    @classmethod
    def extract_sections(cls, 
                         md_path: str, 
                         output_path: str, 
                         granularity: int = 3):
        """
        Extract sections from markdown file with flexible granularity support.
        
        Args:
            md_path: Path to input markdown file
            output_path: Path to output JSON file
            granularity: Maximum section depth (e.g., 3 = up to X.Y.Z)
        """
        with open(md_path, "r", encoding="utf-8") as fp:
            sample_text = fp.read()

        json_out = []

        
        for gran_ in range(2, granularity + 1):
            # Build pattern for specific granularity level
            # Level 1: \d+ (e.g., "6")
            # Level 2: \d+\.\d+ (e.g., "5.6")
            # Level 3: \d+\.\d+\.\d+ (e.g., "5.6.6")
            # etc.
            
            if gran_ == 1:
                prefix = r"\d+"
            else:
                prefix = r"\d+" + (r"\.\d+" * (gran_ - 1))
            
            # Lookahead pattern to catch ANY section number (any granularity)
            lookahead_any_gran = r"\d+(?:\.\d+)*"
            
            # Pattern to match: **X.Y.Z Title text**\n followed by content
            pattern = (
                r"\*\*(?P<num>" + prefix + r")\s+(?P<title>(?:(?!\*\*)[^\n])*?)\*\*\n"
                r"(?P<text>[\s\S]*?)"
                r"(?=\n\*\*" + lookahead_any_gran + r"\s|$)"
            )

            matches = re.finditer(pattern, sample_text)
            matches_list = list(matches)

            for match in tqdm(matches_list, desc=f"Extracting granularity level {gran_}"):
                section_num = match.group('num').strip()
                section_title = match.group('title').strip()
                text = match.group('text')

                # Clean up the extracted text
                clean_text = re.sub(r"Bluetooth SIG Proprietary Page \d+ of \d+", "", text)
                clean_text = re.sub(r"Audio/Video Remote Control Profile / Profile Specification", "", clean_text)
                clean_text = re.sub(r"Basic Audio Profile / Profile Specification", "", clean_text)
                
                # Remove figure captions (text between underscores)
                clean_text = re.sub(r"_Figure \d+(?:\.\d+)*.*?_", "", clean_text)
                clean_text = re.sub(r"_Table \d+(?:\.\d+)*.*?_", "", clean_text)
                
                # Remove excessive whitespace while preserving paragraph structure
                clean_text = re.sub(r"\n\s*\n+", "\n\n", clean_text)
                clean_text = clean_text.strip()

                # Only add if content is not empty
                if clean_text:
                    json_out.append({
                        "section_number": section_num,
                        "section_title": section_title,
                        "granularity_level": gran_,
                        "content": clean_text
                    })

        # Remove duplicates while preserving order
        # (same section might be extracted at different granularity levels)
        seen = set()
        unique_sections = []
        for section in json_out:
            key = (section["section_number"], section["section_title"])
            if key not in seen:
                seen.add(key)
                unique_sections.append(section)

        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(unique_sections, fp, indent=4, ensure_ascii=False)
        
        print(f"\nExtracted {len(unique_sections)} unique sections to {output_path}")


    @classmethod
    def extract_test_cases(cls, md_path: str, output_path: str, pattern: str = None):
        """
        Extract test cases and their subsections from markdown file.
        
        Test case format:
        **BAP/BSRC/SCC/BV-34-C [Test Title]**
        
        Subsections include:
        - Test Purpose
        - Reference
        - Initial Condition
        - Test Procedure
        - Expected Outcome
        
        Args:
            md_path: Path to input markdown file
            output_path: Path to output JSON file
            pattern: Optional custom regex pattern (not used if None)
        """
        with open(md_path, "r", encoding="utf-8") as fp:
            sample_text = fp.read()

        test_case_pattern = r"\*\*(BAP\/.*?)\s+\[(.*?)\]\*\*(.*?)(?=\*\*BAP\/|\*\*\d+\.[\d\.]*|$)"        
        subsection_pattern = r"(Test Purpose|Reference|Initial Condition|Test Procedure|Expected Outcome)\s*\n+((?:(?!\n(?:Test Purpose|Reference|Initial Condition|Test Procedure|Expected Outcome|\*\*BAP\/|\*\*\d+\.)).)*)"
        reference_pattern = r"\b\d+(?:\.\d+){1,}\b"

        matches = re.finditer(test_case_pattern, sample_text, re.DOTALL)
        matches_list = list(matches)

        all_test_cases = []

        for match in tqdm(matches_list, desc="Extracting test cases"):
            test_id = match.group(1).strip()
            test_title = match.group(2).strip()
            content = match.group(3).strip()

            # Extract subsections
            subsection_matches = re.finditer(subsection_pattern, content, re.DOTALL)

            parsed_subsections = []
            for sub_match in subsection_matches:
                sub_title = sub_match.group(1).strip()
                sub_content = sub_match.group(2).strip()

                # Special handling for Reference sections - extract reference numbers
                if sub_title.lower() == "reference":
                    ref_matches = re.finditer(reference_pattern, sub_content)
                    sub_content = list(dict.fromkeys([m.group() for m in ref_matches]))  # Remove duplicates, preserve order

                # Clean up whitespace while preserving structure
                if isinstance(sub_content, str):
                    sub_content = re.sub(r"\n\s+", "\n", sub_content)  # Remove leading whitespace on lines
                    sub_content = re.sub(r"\n\n+", "\n\n", sub_content)  # Collapse multiple newlines
                    sub_content = sub_content.strip()

                # Only add non-empty subsections
                if sub_content:
                    parsed_subsections.append({
                        "title": sub_title,
                        "content": sub_content
                    })

            # Only add test case if it has valid content
            if parsed_subsections:
                all_test_cases.append({
                    "section_id": test_id,
                    "section_title": test_title,
                    "content": parsed_subsections
                })

        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(all_test_cases, fp, indent=4, ensure_ascii=False)

        print(f"\nExtracted {len(all_test_cases)} test cases to {output_path}")


    @classmethod
    def connect_tc_to_req(cls, tc_path : str, req_path : str, output_path : str):
        with open(tc_path, "r", encoding="utf-8") as fp:
            test_cases = json.load(fp)

        with open(req_path, "r", encoding = "utf-8") as fp:
            req = json.load(fp)

        tc_req_mapper = defaultdict(list)

        for case in tqdm(test_cases):
            section_id = case["section_id"]
            references = case["content"][1]["content"]

            for ref in references:
                for requirement in req:
                    req_num = requirement["section_number"]
                    if ref == req_num:
                        tc_req_mapper[section_id].append(requirement)


        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(tc_req_mapper, fp, indent = 4)



class HFPmd(AVRCPmd):


    @classmethod
    def extract_sections(cls, md_path, output_path, granularity = 3):
        return BAPmd.extract_sections(md_path, output_path, granularity)


    @classmethod
    def extract_test_cases(cls, md_path, output_path, pattern = None):
        
        with open(md_path, "r", encoding="utf-8") as fp:
            sample_text = fp.read()

        
        pattern = r"\*\*(HFP\/.*?)\s+\[(.*?)\]\*\*(.*?)(?=\*\*HFP\/|$)"
        sub_pattern = r"-\s*(.*?)\n\n+(.*?)(?=\n-\s*|$)"
        reference_pattern = r"\b\d+(?:\.\d+){2,}\b"

        matches = re.finditer(pattern, sample_text, re.DOTALL)

        all_test_cases = []

        for match in matches:
            section_id = match.group(1).strip()
            section_title = match.group(2).strip()
            content = match.group(3).strip()
    
            cleaned_content = re.sub(r"Bluetooth SIG Proprietary.*?Test Suite", "", content, flags=re.DOTALL)

            sub_matches = re.findall(sub_pattern, cleaned_content, re.DOTALL)

            parsed_data = []
            for title, content in sub_matches:
                # Clean up extra whitespace and newlines
                clean_title = title.strip()
                clean_content = content.strip()

                if clean_title == "Reference":
                    ref_matches = re.finditer(reference_pattern, clean_content)
                    clean_content = [match.group() for match in ref_matches]

                parsed_data.append({
                    "title" : clean_title,
                    "content" : clean_content
                })

            all_test_cases.append({
                "section_id" : section_id,
                "section_title" : section_title,
                "content" : parsed_data
            })

        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(all_test_cases, fp, indent=4, ensure_ascii=False)


class VDPmd:

    @classmethod
    def extract_test_cases(cls, md_path, output_path, pattern = None):
        
        with open(md_path, "r", encoding="utf-8") as fp:
            sample_text = fp.read()

        
        pattern = r"\*\*(VDP\/.*?)\s+\[(.*?)\]\*\*(.*?)(?=\*\*VDP\/|$)"
        sub_pattern = r"-\s*(.*?)\n\n+(.*?)(?=\n-\s*|$)"
        reference_pattern = r"\b\d+(?:\.\d+){2,}\b"

        matches = re.finditer(pattern, sample_text, re.DOTALL)

        all_test_cases = []

        for match in matches:
            section_id = match.group(1).strip()
            section_title = match.group(2).strip()
            content = match.group(3).strip()
    
            cleaned_content = re.sub(r"Bluetooth SIG Proprietary.*?Test Suite", "", content, flags=re.DOTALL)

            sub_matches = re.findall(sub_pattern, cleaned_content, re.DOTALL)

            parsed_data = []
            for title, content in sub_matches:
                # Clean up extra whitespace and newlines
                clean_title = title.strip()
                clean_content = content.strip()

                if clean_title == "Reference":
                    ref_matches = re.finditer(reference_pattern, clean_content)
                    clean_content = [match.group() for match in ref_matches]

                parsed_data.append({
                    "title" : clean_title,
                    "content" : clean_content
                })

            all_test_cases.append({
                "section_id" : section_id,
                "section_title" : section_title,
                "content" : parsed_data
            })

        with open(output_path, "w", encoding="utf-8") as fp:
            json.dump(all_test_cases, fp, indent=4, ensure_ascii=False)

    


class MozillaMd:
    def __init__(self):
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False
        self.converter.ignore_images = True
        self.rouge_scorer = evaluate.load("rouge")


    def extract_sections(self, text : str, type_doc : str = "Mozilla_R1"):

        if type_doc in ["Mozilla_R1", "Mozilla_R2", "Mozilla_R4"]:
            pattern = r'^##\s+(.+?)\n+((?:(?!^##\s)[\s\S])*?)(?=^##\s|\Z)'
        
        if type_doc in ["Mozilla_R3"]:
            pattern = r'^#\s+(.+?)\n+((?:(?!^#\s)[\s\S])*?)(?=^#\s|\Z)'

        sections = re.findall(pattern, text, re.MULTILINE | re.DOTALL)

        results = []

        for title, content in tqdm(sections):
            results.append(
                {
                    "title" : title.replace("#","").strip(),
                    "content" : content.strip()
                }
            )

        return results


    def extract_tc(self, text : str):
        target_sections = ["Purpose", "Initial Conditions", "Steps/Description", "Expected Results", "Description"]
        section_names = "|".join(target_sections)
        pattern = rf"^##\s+({section_names})\n(.*?)(?=\n##|\Z)"
        
        matches = re.findall(pattern, text, re.MULTILINE | re.DOTALL | re.IGNORECASE)
        results = []
        for title, content in matches:
            results.append( {
                "title" : title.strip(),
                "content" : content.strip()
            })

        return results

    def url_to_md(self, url : str):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return self.converter.handle(response.text)
        except requests.exceptions.RequestException as e:
            return None
        

    def extract_links(self, tc_link: str, base_url : str = "https://www-archive.mozilla.org/"):
        match = re.search(r"\[(.*?)\]\((.*?)\)", tc_link)
        if match:
            label = match.group(1)
            link = match.group(2)
            if base_url is None:            
                return {"title" : label,
                        "content" : link 
                        }
            else:
                return {"title" : label,
                        "content" : base_url + link 
                        }
        else:
            return None
        

        
    def extract_feature_tc(self, md: str, type_doc : str = "Mozilla_R1"):
        if type_doc == "Mozilla_R1" or type_doc == "Mozilla_R4":
            pattern = r"^(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*)$"
            results = []
            for line in tqdm(md.strip().split('\n')):
                match = re.search(pattern, line)
                if match:
                    results.append({
                        "feature": match.group(1).strip(),
                        "sub_feature": match.group(2).strip(),
                        "description": match.group(3).strip(),
                        "tc_name": self.extract_links(match.group(4).strip())
                    })
            return results
        
        elif type_doc == "Mozilla_R2" or type_doc == "Mozilla_R3":
            pattern = r"^\s*\|?\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|?\s*$"
            results = []
            for line in tqdm(md.strip().split('\n')):
                match = re.search(pattern, line)
                if match:
                    results.append({
                        "feature": match.group(1).strip(),
                        "description": match.group(2).strip(),
                        "tc_name": self.extract_links(match.group(3).strip())
                    })

            return results


    def make_datasets(self, tc_json : dict):
        augmented_samples = defaultdict(list)

        for tc_ in tqdm(tc_json):
            augmented_samples["feature"].append(tc_["feature"])
            augmented_samples["sub_feature"].append(tc_["sub_feature"])
            augmented_samples["high_level_testcase"].append(tc_["description"])
            augmented_samples["testcase"].append(tc_["test_case"])
            augmented_samples["reference"].append(tc_["reference"])

    
        augmented_samples = datasets.Dataset.from_dict(augmented_samples)
        return augmented_samples
