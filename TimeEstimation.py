import re

def analyze_c_code(file_path):
    # Initialize counters
    total_lines = 0
    complexity = 1  # Cyclomatic complexity starts at 1
    function_count = 0

    # Define regex patterns for control statements and function definitions
    control_statements = [
        r'\bif\b', r'\belse if\b', r'\bfor\b', r'\bwhile\b', r'\bswitch\b', r'\bcase\b', r'\bdefault\b'
    ]
    
    # Updated function pattern to better detect function definitions
    function_pattern = r'^[\w\s\*]+[\w]+\s*\([^)]*\)\s*\{'

    # Open the C file and process it line by line
    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()

            # Count total lines (excluding empty lines and comments)
            if stripped_line and not stripped_line.startswith('//') and not stripped_line.startswith('/*') and not stripped_line.startswith('*'):
                total_lines += 1

            # Check for control structures to calculate cyclomatic complexity
            for pattern in control_statements:
                if re.search(pattern, stripped_line):
                    complexity += 1

            # Check for function definitions
            if re.match(function_pattern, stripped_line):
                function_count += 1

    return total_lines, complexity, function_count

# Example usage
file_path = 'C:\prj\WUP_ENG_BASE_SDP\HAL\RA2E1\ADC\HAL_ADC.c' # Replace with your C file path
lines, complexity, functions = analyze_c_code(file_path)

print(f"Total lines of code: {lines}")
print(f"Cyclomatic complexity: {complexity}")
print(f"Number of functions: {functions}")
