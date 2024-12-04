import time


def find_xmas_patterns_in_grid(grid):
    num_rows = len(grid)
    num_columns = len(grid[0])
    total_xmas_count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for current_row in range(num_rows):
        for current_column in range(num_columns):
            if grid[current_row][current_column] == 'X':
                for direction in directions:
                    current_position = (current_row, current_column)
                    is_valid_pattern = True
                    for i in range(1, 4):
                        current_position = (current_position[0] + direction[0], current_position[1] + direction[1])
                        if not (0 <= current_position[0] < num_rows and 0 <= current_position[1] < num_columns):
                            is_valid_pattern = False
                            break
                        if i == 1 and grid[current_position[0]][current_position[1]] != 'M':
                            is_valid_pattern = False
                            break
                        elif i == 2 and grid[current_position[0]][current_position[1]] != 'A':
                            is_valid_pattern = False
                            break
                        elif i == 3 and grid[current_position[0]][current_position[1]] != 'S':
                            is_valid_pattern = False
                            break
                    if is_valid_pattern:
                        total_xmas_count += 1
    return total_xmas_count


def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            grid = [line.strip() for line in file]
        return find_xmas_patterns_in_grid(grid)
    except Exception as e:
        print("Error opening or processing file:", e)
        return 0


if __name__ == "__main__":
    start_time = time.time()
    result = process_file("../input.txt")
    elapsed_time = time.time() - start_time
    print("Result:", result)
    print(f"Execution time: {elapsed_time:.6f} seconds")
