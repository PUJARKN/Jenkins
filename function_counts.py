import re

def count_c_functions(file_path):
    # Define a regex pattern for detecting C function definitions
    function_pattern = r'^[\w\s\*]+[\w]+\s*\([^)]*\)\s*\{'

    function_count = 0

    # Open the C file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            # Check if the line matches the function definition pattern
            if re.match(function_pattern, stripped_line):
                function_count += 1

    return function_count

# Example usage
file_path = 'C:\prj\WUP_ENG_BASE_SDP\HAL\RA2E1\ADC\HAL_ADC.c'  # Replace with the path to your C file
functions = count_c_functions(file_path)

print(f"Number of functions in the C file: {functions}")
