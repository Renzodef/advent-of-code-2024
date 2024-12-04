import time
import re


def process_file(file_path):
    results_sum = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
                results_sum += sum(int(x) * int(y) for x, y in matches)
        return results_sum
    except Exception as e:
        print("Error opening or processing file:", e)
        return 0


if __name__ == "__main__":
    start_time = time.time()
    result = process_file("../input.txt")
    elapsed_time = time.time() - start_time
    print("Result:", result)
    print(f"Execution time: {elapsed_time:.6f} seconds")
