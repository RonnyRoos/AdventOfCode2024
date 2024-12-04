def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def count_xmas_occurrences(grid):
    def search_word(x, y, dx, dy):
        for i in range(4):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "XMAS"[i]):
                return False
            x += dx
            y += dy
        return True

    directions = [
        (0, 1),  # horizontal right
        (0, -1), # horizontal left
        (1, 0),  # vertical down
        (-1, 0), # vertical up
        (1, 1),  # diagonal down-right
        (1, -1), # diagonal down-left
        (-1, 1), # diagonal up-right
        (-1, -1) # diagonal up-left
    ]

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in directions:
                if search_word(i, j, dx, dy):
                    count += 1
    return count

# Example usage:
file_path = '20241204_01.txt'
grid = read_grid_from_file(file_path)

result = count_xmas_occurrences(grid)
print("Total occurrences of XMAS:", result)