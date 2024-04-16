from openai import OpenAI
import file_export, re, random

# Read API key file
api_key_file = open(".api_key")
api_key = api_key_file.read()

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

# OpenAI API
print("Creating instance of OpenAI")
client = OpenAI(
    api_key = api_key
)

# Run the API
print("API called")
completions = client.chat.completions.create(
  model= model,
  messages=[
    {"role": "system", "content": defensive_prompt},
    {"role": "user", "content": offensive_prompt}
  ]
)
print("API call finished")

# Export results
file_export.write_output_to_folder(defensive_prompt, 
                                   offensive_prompt, 
                                   completions.choices[0].message.content)
