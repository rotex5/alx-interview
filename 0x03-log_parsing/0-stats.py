#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
"""
import sys
from collections import defaultdict

TOTAL_SIZE = 0
STATUS_CODE_COUNTS = defaultdict(int)
LINE_COUNT = 0

for line in sys.stdin:
    # print(line)
    try:
        _, _, _, _, _, _, _, status_code_str, file_size_str = line.split()
        status_code = int(status_code_str)
        file_size = int(file_size_str)
        # print(status_code, file_size)
    except ValueError:
        continue

    TOTAL_SIZE += file_size
    STATUS_CODE_COUNTS[status_code] += 1
    LINE_COUNT += 1

    if LINE_COUNT % 10 == 0:
        print(f"Total file size: {TOTAL_SIZE}")
        for status_code in sorted(STATUS_CODE_COUNTS.keys()):
            count = STATUS_CODE_COUNTS[status_code]
            if count > 0:
                print(f"{status_code}: {count}")

    try:
        # Check if user pressed CTRL + C
        if sys.stdin.isatty() and sys.stdin.read(1) == '\x03':
            print(f"Total file size: {TOTAL_SIZE}")
            for status_code in sorted(STATUS_CODE_COUNTS.keys()):
                count = STATUS_CODE_COUNTS[status_code]
                if count > 0:
                    print(f"{status_code}: {count}")
            sys.exit(0)
    except KeyboardInterrupt:
        # User pressed CTRL + C
        print(f"Total file size: {TOTAL_SIZE}")
        for status_code in sorted(STATUS_CODE_COUNTS.keys()):
            count = STATUS_CODE_COUNTS[status_code]
            if count > 0:
                print(f"{status_code}: {count}")
        sys.exit(0)
