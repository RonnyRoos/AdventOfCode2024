def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def count_xmas_occurrences(grid):
    def search_xmas(x, y):
        # Define the relative positions for the "X-MAS" pattern
        patterns = [
            # Diagonal down-right and diagonal up-left
            [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2)],  # Forward
            [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)],  # Reverse
            # Diagonal down-left and diagonal up-right
            [(0, 2), (1, 1), (2, 0), (2, 2), (0, 0)],  # Forward
            [(0, 2), (1, 1), (2, 0), (0, 0), (2, 2)]   # Reverse
        ]
        
        # Strategy: 
        # - Find the two strings that form the "X-MAS" pattern
        # - Check if they match "MAS" or "SAM"
        # - If they do, return True
        
        # Iterate over each pattern
        for pattern in patterns:
            first_string = ""
            second_string = ""
            # Check each position in the pattern
            for i, (dx, dy) in enumerate(pattern):
                # Calculate the new coordinates
                new_x = x + dx
                new_y = y + dy
                # Check if the new coordinates are within the grid bounds
                if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
                    break
                # Append the character at the new coordinates to the appropriate string
                if i < 3:
                    first_string += grid[new_x][new_y]
                else:
                    second_string += grid[new_x][new_y]
            # Check if the two strings match "MAS" or "SAM"
            if (first_string == "MAS" and second_string == "MS") or (first_string == "SAM" and second_string == "SM"):
                return True
        # If no pattern matches, return False
        return False

    count = 0
    # Iterate over each cell in the grid, excluding the last two rows and columns
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            # Check if the "X-MAS" pattern starts at the current cell
            if search_xmas(i, j):
                count += 1
    return count

# Sample input
sample_grid = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    ".........."
]

# Convert the sample grid to a list of lists
sample_grid = [list(row) for row in sample_grid]

# Test function
def test_count_xmas_occurrences():
    expected_result = 9
    result = count_xmas_occurrences(sample_grid)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"
    print("Test passed!")

# Run the test
test_count_xmas_occurrences()

# Example usage with file input:
file_path = '20241204_01.txt'
grid = read_grid_from_file(file_path)

result = count_xmas_occurrences(grid)
print("Total occurrences of X-MAS in file input:", result)