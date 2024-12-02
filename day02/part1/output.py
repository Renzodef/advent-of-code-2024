import time


def is_safe(report):
    increasing = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):
            return False
        if increasing is None:
            increasing = diff > 0
        elif (increasing and diff <= 0) or (not increasing and diff >= 0):
            return False
    return True


def process_file(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1
    return safe_count


if __name__ == "__main__":
    start_time = time.time()
    result = process_file("../input.txt")
    elapsed_time = time.time() - start_time
    print("Result:", result)
    print(f"Execution time: {elapsed_time:.6f} seconds")
