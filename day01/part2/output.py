import time


def process_file(file_path):
    try:
        first_list = []
        second_list = []
        similarity_score = 0
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    first_list.append(int(parts[0]))
                    second_list.append(int(parts[1]))
        second_list_count = {}
        for num in second_list:
            if num in second_list_count:
                second_list_count[num] += 1
            else:
                second_list_count[num] = 1
        for num in first_list:
            if num in second_list_count:
                num_appearances = second_list_count[num]
                similarity_score += num * num_appearances
        return similarity_score
    except Exception as e:
        print("Error opening or processing file:", e)
        return 0


if __name__ == "__main__":
    start_time = time.time()
    result = process_file("../input.txt")
    elapsed_time = time.time() - start_time
    print("Result:", result)
    print(f"Execution time: {elapsed_time:.6f} seconds")
