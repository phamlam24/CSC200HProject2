from helpers import prompt_test_helper
import re, random

# Manually add defensive and offensive system here
defensive_system = "random_seq_1"
offensive_system = "utilization_attack_2"

# Create defensive prompt from defined language
defensive_prompt_system_file = open("./prompts/defensive/system/" + defensive_system + ".txt")
defensive_prompt = defensive_prompt_system_file.read()

defensive_prompt_secret_file = open("./prompts/defensive/secret/" + defensive_system + ".txt")
secret_prompt = defensive_prompt_secret_file.read()

defensive_prompt = re.sub(r'<SECRET>', 
                          secret_prompt, 
                          defensive_prompt)
defensive_prompt = re.sub(r'<SECRET_NUMBER>', 
                          str(random.randint(1, 1000)), 
                          defensive_prompt)

# Read offensive prompt and modify
offensive_prompt_file = open("./prompts/offensive/" + offensive_system + ".txt")
offensive_prompt = offensive_prompt_file.read()

defensive_wrapperbefore_file = open("./prompts/defensive/wrapper_before/" + defensive_system + ".txt")
wrapper_before = defensive_wrapperbefore_file.read()

defensive_wrapperafter_file = open("./prompts/defensive/wrapper_after/" + defensive_system + ".txt")
wrapper_after = defensive_wrapperafter_file.read()

offensive_prompt = wrapper_before + offensive_prompt + wrapper_after

# Define model
# model = "gpt-4-turbo-2024-04-09"
model = "gpt-3.5-turbo"

# Define number of runs
num_runs = 10

prompt_test_helper.run_prompt_test(defensive_prompt, 
                                       offensive_prompt, 
                                       model,
                                       num_times = 10,
                                       defensive_system = defensive_system,
                                       offensive_system = offensive_system)