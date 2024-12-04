import time


def find_xmas_patterns_in_grid(grid):
    num_rows = len(grid)
    num_columns = len(grid[0])
    total_xmas_count = 0
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for current_row in range(1, num_rows - 1):
        for current_column in range(1, num_columns - 1):
            if grid[current_row][current_column] == 'A':
                m_count = 0
                s_count = 0
                top_left = None
                bottom_right = None
                for direction in directions:
                    next_position = (current_row + direction[0], current_column + direction[1])
                    if 0 <= next_position[0] < num_rows and 0 <= next_position[1] < num_columns:
                        if grid[next_position[0]][next_position[1]] == 'M':
                            m_count += 1
                        elif grid[next_position[0]][next_position[1]] == 'S':
                            s_count += 1
                        if direction == (1, 1):
                            top_left = grid[next_position[0]][next_position[1]]
                        if direction == (-1, -1):
                            bottom_right = grid[next_position[0]][next_position[1]]
                if m_count == 2 and s_count == 2 and top_left != bottom_right:
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
