import evaluate
import uuid
import re
import random
from typing import List, Dict
from utils.generate import OClientModel, OModelConfig


class TCEval:
    def __init__(self, model : OClientModel, default_sections : List[str] = None):
        self.experiment_id = str(uuid.uuid4())
        self.rouge_scorer = evaluate.load("rouge", experiment_id=self.experiment_id)
        self.bleu_scorer = evaluate.load("bleu", experiment_id=self.experiment_id)
        self.bertscore_scorer = evaluate.load("bertscore", experiment_id=self.experiment_id)

        self.model = model

        if default_sections is None:

            self.default_sections = [
                                    "Test Purpose",
                                    "Initial Condition",
                                    "Test Procedure",
                                    "Expected Outcome"
                                    ]
            
        else:

            self.default_sections = default_sections

    def find_sections(self, text : str):
        output = 0

        for section_name in self.default_sections:
            if section_name in text:
                output += 1

        return output / 4
    

    def compare_sections(self, predicted_ : str, reference_ : str):
        

        def parse_predicted(pred_ : str):
            pattern = r"### (.*?):\s*(.*?)(?=###|$)"
            matches = re.findall(pattern, pred_, re.DOTALL)
            parsed_data = {header.strip(): content.strip() for header, content in matches}
            return parsed_data


        
        def parse_reference(ref_ : str):
            target_sections = [
                "Test Purpose", 
                "Initial Condition", 
                "Test Procedure", 
                "Expected Outcome"
            ]

            header_pattern = "|".join(map(re.escape, target_sections))
            pattern = rf"^({header_pattern}):\s*(.*?)(?=^(?:{header_pattern}):|\Z)"
            matches = re.finditer(pattern, ref_, re.MULTILINE | re.DOTALL)
            return {match.group(1).strip(): match.group(2).strip() for match in matches}
        
        score = 0
        target_sections = [
                            "Test Purpose", 
                            "Initial Condition", 
                            "Test Procedure", 
                            "Expected Outcome"
                        ]
        
        try:
            predicted_ = parse_predicted(predicted_)
            reference_ = parse_reference(reference_)

            preds = []
            refs = []

            for sec_ in target_sections:
                p_sec_ = predicted_[sec_]
                r_sec_ = reference_[sec_]

                preds.append(p_sec_)
                refs.append(r_sec_)


            rouge = self.rouge_scorer.compute(predictions=preds, references=refs)
            bleu_1 = self.bleu_scorer.compute(
                                                predictions=preds, 
                                                references=refs,
                                                max_order = 1
                                            )["bleu"]
            
            bleu_2 = self.bleu_scorer.compute(
                                                predictions=preds, 
                                                references=refs,
                                                max_order = 2
                                            )["bleu"]
            
            bleu_4 = self.bleu_scorer.compute(
                                                predictions=preds, 
                                                references=refs,
                                                max_order = 4
                                            )["bleu"]
            
            bertscore_ = self.bertscore_scorer.compute(
                                                    predictions=preds,
                                                    references=refs,
                                                    lang = "en"
                                                )["f1"]
            

            return {
                        "bleu_1": bleu_1,
                        "bleu_2": bleu_2,
                        "bleu_4": bleu_4,
                        "rouge_l": rouge["rougeL"],
                        "bertscore": sum(bertscore_) / len(bertscore_) if bertscore_ else 0.0
                    }

        except:
            return score






    def information_compare(self, 
                            predictions : List[str], 
                            references : List[str]):
        
        def _compare(key_info_1 : List[str], key_info_2 : List[str]):
            """
                key_info_2 has to be reference
            """

            counts = 0

            for key_2 in key_info_2:
                for key_1 in key_info_1:
                    if self.rouge_scorer.compute(predictions = [key_1.lower()], references= [key_2.lower()] )["rougeL"] >= 0.5 : 
                        counts += 1
                        break

            return counts / len(key_info_2)

        
        all_counts = []

        for pred_tc, ref_tc in zip(predictions, references):

            pred_key_info = self.key_information(tc_=pred_tc)
            ref_key_info = self.key_information(tc_=ref_tc)

            all_counts.append(_compare(pred_key_info, ref_key_info))

        return sum(all_counts)/ len(all_counts)
    

    def llm_as_a_judge(self, 
                       prediction : str, 
                       reference : str):
        
        def parse(text : str):
            patterns = {
                "score": r"- Similarity Score:\s*\[?(\d+(?:\.\d+)?)/10\]?",
                "overlaps": r"- Key Overlaps:\s*(.*?)(?=- Key Differences:|$)",
                "differences": r"- Key Differences:\s*(.*)"
            }
            
            results = {
                "similarity_score": None,
                "key_overlaps": None,
                "key_differences": None
            }

            score_match = re.search(patterns["score"], text)
            if score_match:
                results["similarity_score"] = float(score_match.group(1))

            overlaps_match = re.search(patterns["overlaps"], text, re.DOTALL)
            if overlaps_match:
                results["key_overlaps"] = overlaps_match.group(1).strip()

            differences_match = re.search(patterns["differences"], text, re.DOTALL)
            if differences_match:
                results["key_differences"] = differences_match.group(1).strip()

            return results


        
        prompt = f"""Act as a Senior QA Automation Engineer. I will provide two test cases for the same feature. 
Your task is to analyze them and provide a Similarity Score (0-10) based on the following weighted criteria:

1. Initial Conditions: Are the initial condition sections similar?
2. Test Purpose: Are the Test Purpose sections similar?
3. Test Procedure: Are the Test Procedure sections similar?
4. Expected Outcome: Are the Expected Outcome sections similar?

Output Format:
- Similarity Score: [X/10]
- Key Overlaps: [Briefly list what is identical]
- Key Differences: [Briefly list what is unique]

Input Data:
- Test Case A: {prediction}
- Test Case B: {reference}

Only produce output in prescribed format above and nothing else."""
        
        model_config = OModelConfig(temperature=0.7)
        output = self.model(prompt, **model_config.__dict__).response

        results = parse(text = output)

        return results


    def key_information(self, tc_ : str, num_trials : int = 3):
        prompt = f"""Given the following test case find out the key information.
A key information is a very short span (3-6 words) from the text which are very important factually. You must produce the list of key information in comma separated format only.

Output format: key1, key2, key3, key4 ... 

Test Case: {tc_}

Only output your key information in the prescribed format and nothing else."""
        
        all_outputs = []
        
        for _ in range(num_trials):
            config = OModelConfig(temperature=0.7, seed = random.randint(0, 34556))
            output = self.model(prompt, **config.__dict__).response
            output = output.split(",")
            output = [out.strip() for out in output]

            all_outputs.extend(output)

        all_outputs = list(set(all_outputs))
        return all_outputs   