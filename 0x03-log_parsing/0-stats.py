#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
"""
import sys
from collections import defaultdict


total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

for line in sys.stdin:
    # print(line)
    try:
        _, _, _, _, _, _, _, status_code_str, file_size_str = line.split()
        status_code = int(status_code_str)
        file_size = int(file_size_str)
        # print(status_code, file_size)
    except ValueError:
        continue

    total_size += file_size
    status_code_counts[status_code] += 1
    line_count += 1

    if line_count % 10 == 0:
        print(f"Total file size: {total_size}")
        for status_code in sorted(status_code_counts.keys()):
            count = status_code_counts[status_code]
            if count > 0:
                print(f"{status_code}: {count}")

    try:
        # Check if user pressed CTRL + C
        if sys.stdin.isatty() and sys.stdin.read(1) == '\x03':
            print(f"Total file size: {total_size}")
            for status_code in sorted(status_code_counts.keys()):
                count = status_code_counts[status_code]
                if count > 0:
                    print(f"{status_code}: {count}")
            sys.exit(0)
    except KeyboardInterrupt:
        # User pressed CTRL + C
        print(f"Total file size: {total_size}")
        for status_code in sorted(status_code_counts.keys()):
            count = status_code_counts[status_code]
            if count > 0:
                print(f"{status_code}: {count}")
        sys.exit(0)
