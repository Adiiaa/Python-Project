import json
import argparse

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

def read_log_file(file_path, level_filter=None):

    errors = 0
    warnings = 0
    info = 0
    error_counts = {}

    try:
        with open(file_path, "r") as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                timestamp, level, message = parse_log_line(line)
                if level_filter and level != level_filter:
                    continue

                print(f"\nLine {line_number}")
                print(f"Timestamp: {timestamp}")
                print(f"Level: {level}")
                print(f"Message: {message}")
                if level == "ERROR":
                    errors += 1

                    if message in error_counts:
                        error_counts[message] += 1
                    else:
                        error_counts[message] = 1

                elif level == "WARNING":
                    warnings += 1

                elif level == "INFO":
                    info += 1

        if error_counts:
            most_common_error = max(
                error_counts,
                key=error_counts.get
            )
        else:
            most_common_error = "No errors found"

        print("\n===== SUMMARY =====")
        print(f"Errors:   {errors}")
        print(f"Warnings: {warnings}")
        print(f"Info:     {info}")
        print(f"Most frequent error: {most_common_error}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--level")

    args = parser.parse_args()

    read_log_file("sample.log", args.level)