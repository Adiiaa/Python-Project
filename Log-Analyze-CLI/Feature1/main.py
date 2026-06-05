def read_log_file(file_path):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")
if __name__ == '__main__':
    read_log_file("sample.log")