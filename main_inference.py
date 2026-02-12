import argparse
from functools import partial
from utils.rl_trainer import PRLTrainer
from utils.prepare_dataset import RLPRLDataset
from utils.generate import OClientModel, OModelConfig
from utils.rewards import RewardFuncs


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Ans Extraction Inference Arguments")

    parser.add_argument("--policy_model_name", type = str, help = "Base Policy Model name", default="unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit")
    parser.add_argument("--lora_adapter_path", type = str, help = "Lora Adapter Path")
    parser.add_argument("--ollama_model_name", type=str, help="ollama model name")
    parser.add_argument("--port", help="ollama port", type=str)
    parser.add_argument("--max_seq_len", type = int, default=16000, help = "Maximum Sequence Length")
    parser.add_argument("--max_prompt_len", type = int, default = 4196)
    parser.add_argument("--lora_rank", type=int, help="Lora Rank", default=64)
    parser.add_argument("--temperature", type = float, default = 0.7)
    parser.add_argument("--top_p", type = float, default = 0.9)
    parser.add_argument("--num_sequences", type = int, default=5)
    parser.add_argument("--seed", type = int, default=42)


    args = parser.parse_args()

    model = OClientModel(model_name=args.ollama_model_name, port=args.port)
    config = OModelConfig()


    system_prompt = """You are an automative expert who specializes in generating diverse and effective prompts for generating test specifications for another model. Your primary goal is to analyze a given purpose and requirements, generate a *new, refined prompt* that aims to elicit a different, yet highly effective, set of answers.

Your entire response MUST follow a strictly defined structure with four main sections enclosed in specific tags:

1.  **<think>...</think>**: Detail your reasoning and analyze how to build the prompt.
2.  **<requirement analysis>...</requirement analysis>**: Provide an analysis of the requirements in the inputs from the expected output.
3.  **<verification analysis>...</verification analysis>**: Provide an analysis of the verification criteria present in the inputs from the expected output.
4.  **<quality analysis>...</quality analysis>**: Provide an analysis how quality of new prompt should be judged.
5.  **<output structure analysis>...</output structure analysis>**: Provide an analysis for the output structure in the output.
6.  **<prompt>...</prompt>**: Provide your new refined prompt.

### Response Format:

<think>
[Detailed analysis of the base prompt and strategy for refinement goes here. Focus on identifying and mitigating narrow focus or low diversity in potential answers.]
</think>
<requirement analysis>
[Analysis of the requirements in the inputs, focusing on testable parameters and completeness.]
</requirement analysis>
<verification analysis>
[Analysis of the necessary verification criteria, emphasizing measurability and pass/fail conditions.]
</verification analysis>
<quality analysis>
[Analysis of how the new prompt's quality should be judged (e.g., novelty, specificity, utility of the generated output).]
</quality analysis>
<output structure analysis>
[Analysis of the mandatory structured output format (e.g., JSON, Markdown table) required from the final prompt.]
</output structure analysis>
<prompt>
[The complete, actionable new prompt string goes here.]
</prompt>"""
        
    base_task_prompt = """Given an input and output pair, produce the prompt that produced the output for the input. The output must be a JSON compatible.
<input>
Purpose: Verify TCS+ availability and no LTCS+ activation within 1.2 seconds after ignition ON during normal drive-off on a standard surface.

Requirements & Verification Criteria

R1 — Availability (ESP)
Requirement (summarized):

TCS+ shall become fully available ≤ 1.2 s after ignition ON.
A temporary performance compromise during early parameter identification (e.g., tyre radii) is acceptable, but full performance must be reached within 2 km of driving under normal conditions (straight-ahead and moderate torque).
If signal quality is sufficient, no signal monitoring shall keep traction deactivated.
Legal requirements must be met at all times.
Background: certain identification routines (learning, sensor checks, tyre tolerance) need time to complete.

RB Verification Criteria (R1):
Drive off immediately after ignition ON (engine running) on low-μ surface: TCS+ engages ≈ 1.2 s after ignition ON.
Traction: 70% of the max possible acceleration shall be reached within a certain (situation-dependent) time; delay depends on driving situation and reference speed initialization.

R2 — Proper operation when switching SYSTEM-OFF → SYSTEM-ON while rolling
Requirement (summarized):
The system shall operate properly when switching from SYSTEM-OFF to SYSTEM-ON (with ignition) while the vehicle is rolling.
Note: SYSTEM-ON/OFF modes are defined in the ESP System Requirements Spec (SysRS) and the System Architecture for ESP.

RB Verification Criteria (R2):
On a standard surface with engine ON, move to low-μ, perform ignition OFF, then ON, apply throttle: if all sensors are operational, TCS+ shall be available.
With the vehicle rolling, switch to ignition ON, then immediately provoke a TCS+ intervention (e.g., accelerate on low-μ) → TCS+ works immediately.

Test Design
Techniques: State Transition Testing; Decision Table Testing; Equivalence Class/Partitioning.
State Model (high-level)
TCS_Off (system not available)
→ Ignition ON, sensors OK, standard/low-μ → TCS_Initializing
TCS_Initializing
→ Init complete, < 1.2 s after ignition ON → TCS_Available
TCS_Available
→ Low-μ + high accel demand (e.g., pedal 95%) → TCS_Active
→ Standard surface + moderate accel (≤ 25%) → TCS_Available
→ Ignition OFF → TCS_Off
TCS_Active
→ Traction restored / demand removed → TCS_Available
→ Ignition OFF → TCS_Off
Scenario (from design)
1. TCS_Off → (Ignition ON, sensors OK, standard surface) → TCS_Initializing
2. TCS_Initializing → Init complete < 1.2 s after ignition ON → TCS_Available
3. TCS_Available → (Standard surface, accel ≤ 25%) → TCS_Available
</input>
<output>
{
  "test_spec_name": "Improved Test Spec",
  "notes": "This test verifies TCS+ availability within 1.2 s after ignition ON and confirms no LTCS+ activation during normal drive-off on a standard surface. All sensors must be operational; the vehicle must be stationary before measurement begins.",
  "preconditions": [
    {
      "id": "P1",
      "description": "Turn System ON",
      "stimulation": "Set battery to 12.6V; switch ignition OFF",
      "expected": "—"
    },
    {
      "id": "P2",
      "description": "Vehicle in standstill",
      "stimulation": "Gear Drive; Accel 0%; Brake 0%",
      "expected": "—"
    },
    {
      "id": "P3",
      "description": "Clear failure memory",
      "stimulation": "Clear Bosch, Customer, OBD memories",
      "expected": "Failure memories are empty (online eval: true)"
    },
    {
      "id": "P4",
      "description": "Full System",
      "stimulation": "Evaluate lamp states per Full_System strategy",
      "expected": "—"
    },
    {
      "id": "P5",
      "description": "Set default μ surface",
      "stimulation": "Road friction 0.85 / 0.85 (L/R wheels)",
      "expected": "—"
    }
  ],
  "actions_steps": [
    {
      "id": "A1",
      "description": "Start Measurement",
      "stimulation_maneuver": "Begin trace recording for all recording groups",
      "expected": "Recording active; signals logging (online eval: false)"
    },
    {
      "id": "A2",
      "description": "Ignition ON",
      "stimulation_maneuver": "Switch ignition to ON",
      "expected": "TCS+ fully available ≤ 1.2 s after ignition ON (online eval: true)"
    },
    {
      "id": "A3",
      "description": "Apply moderate accel",
      "stimulation_maneuver": "Increase accelerator linearly to 25%",
      "expected": "sDrvPedalRaw ≥ 24 (online eval: false)"
    },
    {
      "id": "A4",
      "description": "Release accel",
      "stimulation_maneuver": "Set accelerator to 0%",
      "expected": "—"
    },
    {
      "id": "A5",
      "description": "Apply brake",
      "stimulation_maneuver": "Set brake to 40%",
      "expected": "—"
    },
    {
      "id": "A6",
      "description": "Release brake",
      "stimulation_maneuver": "Set brake to 0%",
      "expected": "—"
    },
    {
      "id": "A7",
      "description": "Read failure memories",
      "stimulation_maneuver": "Read Bosch & Customer memories",
      "expected": "Failure memories empty (online eval: true)"
    },
    {
      "id": "A8",
      "description": "Read lamps",
      "stimulation_maneuver": "Evaluate LTCS+ lamp state",
      "expected": "LTCS+ OFF; no activation/blink (online eval: false)"
    },
    {
      "id": "A9",
      "description": "Stop Measurement",
      "stimulation_maneuver": "Stop trace recording",
      "expected": "Recording stopped (online eval: false)"
    }
  ],
  "postconditions": [
    {
      "id": "C1",
      "description": "Read lamps",
      "stimulation": "Evaluate LTCS+ lamp state",
      "expected": "LTCS+ OFF; no activation/blink"
    },
    {
      "id": "C2",
      "description": "Undo manipulations",
      "stimulation": "Reset road friction to 0.85 for all wheels",
      "expected": "—"
    }
  ]
}
</output>"""


    prl = PRLTrainer(policy_model_name=args.policy_model_name, 
                                lora_rank=int(args.lora_rank),
                                max_seq_len=int(args.max_seq_len), 
                                is_inference=True,
                                lora_adapter_name=args.lora_adapter_path,
                                use_vllm=True)
    
    generated_sequences = prl.generate_inference(base_task_prompt=base_task_prompt,
                                                           system_prompt=system_prompt,
                                                           num_sequences=int(args.num_sequences), 
                                                           temperature=float(args.temperature),
                                                           top_p=float(args.top_p),
                                                           max_seq_len=int(args.max_seq_len))

    sequences = [seq["prompt_with_think"] for seq in generated_sequences]
    

    for seq in sequences:
        print(seq)
        print("\n\n\n")





    
     




