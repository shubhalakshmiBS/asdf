def extract_functions_name(code):
    # Regular expression to match function declarations and comments in Python
    pattern = r'\bdef\s+([\w\d_]+)\(.*?\):\s+'  # Pattern for function definitions
    function_names = re.findall(pattern, code)
    print(f"fun name ==================={function_names}")
    
    return function_names