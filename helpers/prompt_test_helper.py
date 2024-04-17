from openai import OpenAI
from helpers import file_export

# This function takes a defensive prompt, an offensive prompt, and a model
# Returns results in the run_results folder. Interpretations of the results 
# are left for the user.
def run_one_prompt_test(defensive_prompt, offensive_prompt, model):
    # Read API key file
    api_key_file = open(".api_key")
    api_key = api_key_file.read()

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
                                    completions.choices[0].message.content,
                                    model)
    
# This function takes a defensive prompt, an offensive prompt, and a model
# Returns results in the run_results folder. Interpretations of the results 
# are left for the user.
# This function instead runs multiple times
def run_prompt_test(defensive_prompt, offensive_prompt, model = "gpt-3.5-turbo", num_times = 1):
    # Read API key file
    api_key_file = open(".api_key")
    api_key = api_key_file.read()

    # OpenAI API
    print("Creating instance of OpenAI")
    client = OpenAI(
        api_key = api_key
    )

    # Run the API
    print("API called")
    completions = client.chat.completions.create(
    model = model,
    messages=[
        {"role": "system", "content": defensive_prompt},
        {"role": "user", "content": offensive_prompt}
    ],
    n = num_times
    )
    print("API call finished")

    results = []
    for choice in completions.choices:
        results.append(choice.message.content)
    file_export.write_outputlist_to_folder(defensive_prompt,
                                           offensive_prompt,
                                           results,
                                           model)