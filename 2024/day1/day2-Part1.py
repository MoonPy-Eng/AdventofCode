def check_safe(report):
    # Check if all levels are increasing or decreasing
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    if not (increasing or decreasing):
        return "Unsafe"

    # Check if differences between all adjacent levels are within the range [1, 3]
    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i + 1])
        if difference < 1 or difference > 3:
            return "Unsafe"

    return "Safe"

def process_reports(file_path):
    safe_count = 0
    unsafe_count = 0

    # Open and read the file line by line
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Ignore empty lines
                if not line.strip():
                    continue

                # Convert the line to a list of integers
                try:
                    report = list(map(int, line.strip().split()))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue

                # Check the safety of the report
                result = check_safe(report)
                if result == "Safe":
                    safe_count += 1
                else:
                    unsafe_count += 1

        # Output the total counts of safe and unsafe reports
        print(f"Safe reports: {safe_count}")
        print(f"Unsafe reports: {unsafe_count}")
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program with the file 'day2_data.txt'
process_reports('day2_data.txt')
