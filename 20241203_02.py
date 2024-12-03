import re

def extract_and_multiply(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    
    # Regular expressions to find valid mul(X,Y), do(), and don't() instructions
    mul_pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")
    
    total_sum = 0
    enabled = True  # Initially, mul instructions are enabled
    
    # Split the data into tokens based on the patterns
    tokens = re.split(r'(mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don\'t\(\))', data)
    
    for token in tokens:
        if mul_pattern.match(token):
            if enabled:
                x, y = map(int, mul_pattern.findall(token)[0])
                total_sum += x * y
        elif do_pattern.match(token):
            enabled = True
        elif dont_pattern.match(token):
            enabled = False
    
    return total_sum

# Example usage:
file_path = '20241203_01.txt'
result = extract_and_multiply(file_path)

print("Total sum of valid multiplications:", result)