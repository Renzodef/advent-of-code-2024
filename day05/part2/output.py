import time


def reorder_numbers(numbers, rules):
    changed = True
    while changed:
        changed = False
        for a, b in rules:
            if a in numbers and b in numbers:
                a_index = numbers.index(a)
                b_index = numbers.index(b)
                if a_index > b_index:
                    numbers[a_index], numbers[b_index] = numbers[b_index], numbers[a_index]
                    changed = True
    return numbers


def process_file(file_path):
    try:
        rules = []
        middle_number_reordered_lines_sum = 0
        with open(file_path, 'r') as file:
            lines = file.readlines()
        blank_line_index = lines.index("\n")
        rules_part = lines[:blank_line_index]
        numbers_part = lines[blank_line_index + 1:]
        for numbers in rules_part:
            a, b = map(int, numbers.strip().split('|'))
            rules.append((a, b))
        for line in numbers_part:
            numbers = list(map(int, line.strip().split(',')))
            valid = True
            for a, b in rules:
                if a in numbers and b in numbers:
                    if numbers.index(a) > numbers.index(b):
                        valid = False
                        break
            if not valid:
                reordered = reorder_numbers(numbers, rules)
                middle_number_reordered_lines_sum += reordered[len(reordered) // 2]
        return middle_number_reordered_lines_sum
    except Exception as e:
        print("Error opening or processing file:", e)
        return 0


if __name__ == "__main__":
    start_time = time.time()
    result = process_file("../input.txt")
    elapsed_time = time.time() - start_time
    print("Result:", result)
    print(f"Execution time: {elapsed_time:.6f} seconds")
