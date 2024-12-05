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

def topological_sort(update, rules):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = {page: 0 for page in update}

    for x, y in rules:
        if x in in_degree and y in in_degree:
            graph[x].append(y)
            in_degree[y] += 1

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def calculate_middle_pages_sum(file_path):
    lines = read_grid_from_file(file_path)
    rules, updates = parse_input(lines)
    
    correct_updates = [update for update in updates if is_update_correct(update, rules)]
    incorrect_updates = [update for update in updates if not is_update_correct(update, rules)]
    
    middle_pages_sum_correct = sum(find_middle_page(update) for update in correct_updates)
    middle_pages_sum_incorrect = sum(find_middle_page(topological_sort(update, rules)) for update in incorrect_updates)
    
    return middle_pages_sum_correct, middle_pages_sum_incorrect

# Test function
def test_calculate_middle_pages_sum():   
    # Run the calculate_middle_pages_sum function with the sample input
    correct_sum, incorrect_sum = calculate_middle_pages_sum('20241205_01_sample_input.txt')
    
    # Expected results
    expected_sum = 123
    
    # Check if the results match the expected results
    assert incorrect_sum == expected_sum, f"Expected {expected_sum}, but got {incorrect_sum}"
    print("Test passed!")

# Run the test
test_calculate_middle_pages_sum()

# Example usage with file input:
file_path = '20241205_01.txt'
correct_sum, incorrect_sum = calculate_middle_pages_sum(file_path)
print("Sum of middle page numbers from correctly-ordered updates:", correct_sum)
print("Sum of middle page numbers after correctly ordering incorrect updates:", incorrect_sum)