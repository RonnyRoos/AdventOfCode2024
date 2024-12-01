def read_numbers_from_file(file_path):
    list1 = []
    list2 = []
    
    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    
    list1.sort()
    list2.sort()

    return list1, list2

def compare_lists(list1, list2):
    comparisons = []
    for num1, num2 in zip(list1, list2):
        comparisons.append(abs(num1 - num2))
    return comparisons

# Example usage:
file_path = '20241201_01_numbers.txt'
list1, list2 = read_numbers_from_file(file_path)
comparisons = compare_lists(list1, list2)


# Sum all the numbers in the comparisons list
total_comparison_sum = sum(comparisons)

print(total_comparison_sum)