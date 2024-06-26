from helpers import prompt_test_helper
import re, random

# Read defensive prompt, replacing <SECRET_NUMBER> 
# with a random number in the range [1, 1000]
defensive_prompt_file = open("./prompts/defensive_prompt.txt")
defensive_prompt = defensive_prompt_file.read()
defensive_prompt = re.sub(r'<SECRET_NUMBER>', 
                          str(random.randint(1, 1000)), 
                          defensive_prompt)

# Read offensive prompt
offensive_prompt_file = open("./prompts/offensive_prompt.txt")
offensive_prompt = offensive_prompt_file.read()

# Define model
# model = "gpt-4-turbo-2024-04-09"
model = "gpt-3.5-turbo"

# Define number of results
num_runs = 10

# Run test
prompt_test_helper.run_prompt_test(defensive_prompt, offensive_prompt, model, num_runs)