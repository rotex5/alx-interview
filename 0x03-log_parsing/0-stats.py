#!/usr/bin/python3
"""

-Write a script that reads stdin line by line and computes metrics:

-Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size> (if the format is not this one, the
                           line must be skipped)

-After every 10 lines and/or a keyboard interruption (CTRL + C),
    print these statistics from the beginning:
*Total file size: File size: <total size>
*where <total size> is the sum of all previous <file size>
    (see input format above)

*Number of lines by status code:
+possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
+if a status code doesn’t appear or is not an integer, don’t print
    anything for this status code
+format: <status code>: <number>
+status codes should be printed in ascending order

Log parsing
Reads stin line by line and computes metrics
(i.e <status code> and <file size>)

'104.245.160.235 - [2023-05-12 01:45:51.041606]
"GET /projects/260 HTTP/1.1" 200 251'

output:
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
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
