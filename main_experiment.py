from helpers import prompt_test_helper
import re, random, os


def get_files_in_folder(folder_path):
    # Get the list of files and directories in the specified folder
    files_and_dirs = os.listdir(folder_path)
    
    # Filter out only the file names
    file_names = [os.path.splitext(file)[0] for file in files_and_dirs if os.path.isfile(os.path.join(folder_path, file))]

    return file_names


# Define variables here!!
model = "gpt-3.5-turbo"
num_results = 20

if __name__ == "__main__":
    offensive_methods = get_files_in_folder("./prompts/offensive")
    defensive_methods = get_files_in_folder("./prompts/defensive/system")
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Navigate to the "run_results" folder or create it if it doesn't exist
    run_results_dir = os.path.join(current_dir, "run_results")
    if not os.path.exists(run_results_dir):
        os.makedirs(run_results_dir)
    
    # Find the lowest positive number X that does not have a folder named with that number
    x = 1
    while os.path.exists(os.path.join(run_results_dir, str(x))):
        x += 1
    
    # Create a folder named X
    folder_path = os.path.join(run_results_dir, str(x))
    os.makedirs(folder_path)



    for offensive_system in offensive_methods:
        for defensive_system in defensive_methods:
            
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

            output_file_path = os.path.join(folder_path, offensive_system + "-" + defensive_system + ".txt")

            output_file = open(output_file_path, "w")
            output_file.write("Defensive Prompt: " + defensive_system + ":\n")
            output_file.write(defensive_prompt)
            output_file.write("\n\n~~~~~~~~~~\n\n")
            output_file.write("Offensive Prompt - " + offensive_system + ":\n")
            output_file.write(offensive_prompt)
            output_file.write("\n\n~~~~~~~~~~\n\n")

            # Get results
            outputs = prompt_test_helper.prompt_test(defensive_prompt, offensive_prompt,
                                           model = model, num_times = num_results,
                                           defensive_system = defensive_system,
                                           offensive_system = offensive_system)
            i = 1
            for output in outputs:
                output_file.write(model + " output #" + str(i) +":\n")
                output_file.write(output)
                output_file.write("\n\n")
                i += 1
            output_file.close()
