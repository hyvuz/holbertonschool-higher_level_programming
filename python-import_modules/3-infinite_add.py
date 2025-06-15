#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    for i in range(1, len(sys.argv)):  # Skip the script name at index 0
        result += int(sys.argv[i])     # Convert and add each argument

    print(result)
