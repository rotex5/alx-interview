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
    try:
        _, _, _, _, _, _, _, status_code_str, file_size_str = line.split()
        status_code = int(status_code_str)
        file_size = int(file_size_str)
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
