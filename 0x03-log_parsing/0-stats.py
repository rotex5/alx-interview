#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
"""
import sys


def logParser():
    """
    Reads stdin line by line
    """
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    counter = 0

    try:
        for line in sys.stdin:
            _, _, _, _, _, _, _, code_str, file_size_str = line.split()
            if code_str and file_size_str:
                size = int(file_size_str)
                if code_str in status_codes.keys():
                    status_codes[code_str] += 1
                total_size += size
                counter += 1

            if counter == 10:
                logDisplay(total_size, status_codes)
                counter = 0
        logDisplay(total_size, status_codes)

    except Exception as e:
        pass

    finally:
        logDisplay(total_size, status_codes)



def logDisplay(total_size, status_codes):
    """
    Outputs computed metric from logParser()
    """
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


if __name__ == '__main__':
    logParser()
