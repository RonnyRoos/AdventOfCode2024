def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

def parse_input(lines):
    rules = []
    updates = []
    parsing_rules = True
    for line in lines:
        if line == "":
            parsing_rules = False
            continue
        if parsing_rules:
            rules.append(tuple(map(int, line.split('|'))))
        else:
            updates.append(list(map(int, line.split(','))))
    return rules, updates

def is_update_correct(update, rules):
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def calculate_middle_pages_sum(file_path):
    lines = read_grid_from_file(file_path)
    rules, updates = parse_input(lines)
    
    correct_updates = [update for update in updates if is_update_correct(update, rules)]
    middle_pages_sum = sum(find_middle_page(update) for update in correct_updates)
    
    return middle_pages_sum

# Test function
def test_calculate_middle_pages_sum():

    
    # Run the calculate_middle_pages_sum function with the sample input
    result = calculate_middle_pages_sum('20241205_01_sample_input.txt')
    
    # Expected result
    expected_result = 143
    
    # Check if the result matches the expected result
    assert result == expected_result, f"Expected {expected_result}, but got {result}"
    print("Test passed!")

# Run the test
test_calculate_middle_pages_sum()

# Example usage with file input:
file_path = '20241205_01.txt'
result = calculate_middle_pages_sum(file_path)
print("Sum of middle page numbers from correctly-ordered updates:", result)