import re

def extract_and_multiply(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    
    # Regular expression to find valid mul(X,Y) instructions
    pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')
    matches = pattern.findall(data)
    
    total_sum = 0
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y
    
    return total_sum

# Example usage:
file_path = '20241203_01.txt'
result = extract_and_multiply(file_path)

print("Total sum of valid multiplications:", result)