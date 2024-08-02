#!/usr/bin/python3
"""
This module cotains several fcuntions.
"""
import sys
import re
import signal


def print_stats(total_size, status_counts):
    """
    Print the total file size and the number of lines by status code.

    Parameters:
    - total_size: The sum of all file sizes.
    - status_counts: A dictionary with status codes as
    keys and their counts as values.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def parse_line(line):
    """
    Parse a single log line to extract the status code and file size.

    Parameters:
    - line: A string representing a single log line.

    Returns:
    - (status_code, file_size): A tuple containing the status code
    and file size if the line matches the format,
      otherwise (None, None).
    """
    regex = r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    match = re.match(regex, line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        return status_code, file_size
    return None, None


def main():
    """
    Main function to process log lines from standard input, compute statistics,
    and handle keyboard interrupts.
    """
    total_size = 0
    line_count = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }

    def signal_handler(sig, frame):
        """
         Signal handler for keyboard interrupts (CTRL + C).

        Parameters:
        - sig: Signal number.
        - frame: Current stack frame.
        """
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line.strip())
            if status_code is not None and file_size is not None:
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
                line_count = 0
    except Exception as e:
        pass

    finally:
        print_stats(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
