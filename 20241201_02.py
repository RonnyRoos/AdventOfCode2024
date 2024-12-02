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

def calculate_similarity_score(list1):
    score = 0
    for num in list1:
        score += num * list2.count(num)
    return score

# Example usage:
file_path = '20241201_01.txt'
list1, list2 = read_numbers_from_file(file_path)

print(calculate_similarity_score(list1))