from utils.generate import OClientModel, OModelConfig
import json
import re



class LLM_as_Judge:
    def __init__(self, model : OClientModel, config : OModelConfig):
        self.model = model
        self.config = config

    
    def _to_json(self, response_string : str):
        try:
            clean_content = re.sub(r'```json|```', '', response_string).strip()
            
            data = json.loads(clean_content)
            return data
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            return None
        
    def _to_json_llm(self, response_string : str, num_trials : int = 3):
        try:
            clean_content = re.sub(r'```json|```', '', response_string).strip()
            
            data = json.loads(clean_content)
            return data
        
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON object: {e}, using LLM to generate a json")
            system_prompt = """You are an expert Software Engineer who transform information which is not in json format into correct json format.
Your goal is to act as 'Judge' to evaluate the information provided to turn it into a json object with respect to the keys provided."""

            prompt = f"""Extract the valuable information from the following text and output the information in json format.
### Text:
{response_string}

### OUTPUT JSON FORMAT:
Return only a JSON object with these keys:
"score": (int),
"alignment_index": (string: "High"|"Medium"|"Low"),
"technical_critique": (string),
"missing_elements": (list of strings),
"is_fine_tuning_ready": (boolean)

Only produce your output in above format and nothing else."""
            
            output = self.model(prompt=prompt, system_prompt = system_prompt, **self.config.__dict__).response

            return self._to_json(response_string=output)


    def __call__(self, 
                 tc : dict, 
                 req : dict,
                 num_trials : int = 5):

        system_prompt = """
You are a Senior Bluetooth Protocol Engineer and QA Architect specialized in the Bluetooth Core Specification (v5.0 - v5.4). 
Your goal is to act as a 'Judge' to evaluate the quality of a dataset entry that maps a technical requirement to a test case.

You must evaluate the pair based on:
1. Technical Fidelity: Does the test case utilize the correct protocol layers (HCI, L2CAP, ATT, etc.)?
2. Logical Soundness: Do the steps lead to the verification of the requirement?
3. Pass/Fail Clarity: Is the expected result unambiguous and grounded in the specification?
4. Atomicity: Is the test case focused only on the provided requirement?

You will output your evaluation in a structured JSON format including a numerical score and technical reasoning.
"""


        prompt = f"""
Evaluate the following Bluetooth Dataset Pair:

### REQUIREMENT:
{req}

### TEST CASE:
{tc}

### SCORING RUBRIC:
- 5 (Excellent): Test case is technically perfect, covers all aspects of the requirement, uses correct Bluetooth terminology, and has clear verification steps.
- 4 (Good): Valid test case but might have minor wordiness or lack one small edge case mentioned in the requirement.
- 3 (Fair): The test case is related to the requirement but is generic or lacks specific Bluetooth parameters (e.g., missing specific HCI commands or timers).
- 2 (Poor): Significant technical gaps. The test case fails to verify the core logic of the requirement.
- 1 (Invalid): Hallucinated content, incorrect protocol logic, or the test case does not match the requirement at all.

### OUTPUT FORMAT:
Return only a JSON object with these keys:
"score": (int),
"alignment_index": (string: "High"|"Medium"|"Low"),
"technical_critique": (string),
"missing_elements": (list of strings),
"is_fine_tuning_ready": (boolean)

Only produce your output in above format and nothing else.
"""
        
        output = self.model(prompt=prompt, 
                            system_prompt = system_prompt,
                            **self.config.__dict__).response

        return self._to_json_llm(response_string=output)

