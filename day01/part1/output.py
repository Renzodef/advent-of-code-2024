import time


def process_file(file_path):
    try:
        first_list = []
        second_list = []
        total_distance = 0
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    first_list.append(int(parts[0]))
                    second_list.append(int(parts[1]))
        first_list.sort()
        second_list.sort()
        for val1, val2 in zip(first_list, second_list):
            total_distance += abs(val1 - val2)
        return total_distance
    except Exception as e:
        print("Error opening or processing file:", e)
        return 0


if __name__ == "__main__":
    start_time = time.time()
    result = process_file("../input.txt")
    elapsed_time = time.time() - start_time
    print("Result:", result)
    print(f"Execution time: {elapsed_time:.6f} seconds")
