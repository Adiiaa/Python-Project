import json

def parse_log_line(line):
    try:
        log_data = json.loads(line)
        timestamp= log_data['timestamp']
        level = log_data['level']
        message = log_data['message']
        return timestamp, level, message
    except json.JSONDecodeError:
        parts = line.split()
        timestamp = parts[0]+ " "+ parts[1]
        level = parts[2]
        message = " ".join(parts[3:])
        return timestamp, level, message

def read_log_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                timestamp, level, message = parse_log_line(line)
                print(f"\nLine {line_number}")
                print(f"Timestamp: {timestamp}")
                print(f"Level: {level}")
                print(f"Message: {message}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
if __name__ == '__main__':
    read_log_file("sample.log")