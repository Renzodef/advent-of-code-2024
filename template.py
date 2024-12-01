import time

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
        return 0
    except Exception as e:
        print("Error opening or processing file:", e)
        return 0

if __name__ == "__main__":
    start_time = time.time()
    result = process_file("../input.txt")
    elapsed_time = time.time() - start_time
    print("Result:", result)
    print(f"Execution time: {elapsed_time:.6f} seconds")
