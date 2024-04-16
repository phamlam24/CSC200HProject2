import os

def write_output_to_folder(defensive_prompt, offensive_prompt, output):
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
    
    # Create a file named "output.txt" and write the results to that file
    output_file_path = os.path.join(folder_path, "output.txt")
    with open(output_file_path, "w") as output_file:
        output_file.write("Defensive Prompt:\n")
        output_file.write(defensive_prompt)
        output_file.write("\n\n~~~~~~~~~~\n\n")
        output_file.write("Offensive Prompt:\n")
        output_file.write(offensive_prompt)
        output_file.write("\n\n~~~~~~~~~~\n\n")
        output_file.write("gpt-4-turbo output:\n")
        output_file.write(output)


