import os
import re
import argparse
import matplotlib.pyplot as plt
from typing import List, Tuple
import numpy as np


def extract_reward_values(log_text: str) -> List[Tuple[str, float]]:
    """
    Finds all instances of 'reward' and its associated numerical value in the log text.
    """
    # Regex pattern: 
    # 'reward': matches the literal key
    # '\s*:\s*': matches colon with optional whitespace
    # '(-?\d+\.?\d*e?-?\d*)': captures the float (including negatives and scientific notation)
    pattern = r"'reward'\s*:\s*(-?\d+\.?\d*e?-?\d*)"
    
    # re.findall returns a list of captured groups (the values)
    reward_values_str = re.findall(pattern, log_text)
    
    # Convert captured string values to floats and pair with the key 'reward'
    results = []
    for value_str in reward_values_str:
        try:
            results.append(('reward', float(value_str)))
        except ValueError:
            # Skip if conversion fails (shouldn't happen with this specific log format)
            continue
            
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--log_file", type = str, help = "Log file where losses and rewards are given")

    args = parser.parse_args()
    
    results = []
    with open(args.log_file, "r") as fp:
        for line in fp.readlines():
            line_result = extract_reward_values(log_text=line)

            results.append(line_result)

    results = [res[0][1] for res in results if len(res) > 0]

    if results:
        rewards_array = np.array(results)
        running_mean = np.cumsum(rewards_array) / np.arange(1, len(rewards_array) + 1)

        # 3. Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(rewards_array, 'o', label='Individual Reward', alpha=0.5)
        plt.plot(running_mean, '-', color='red', linewidth=2, label='Running Mean')

        plt.title('Running Mean of Training Reward', fontsize=16)
        plt.xlabel('Log Entry Index (or Step)', fontsize=12)
        plt.ylabel('Reward Value', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.xticks(np.arange(len(rewards_array)), np.arange(1, len(rewards_array) + 1))
        
        plt.savefig('running_mean_reward_plot.png')




