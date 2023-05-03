#!/usr/bin/python3
"""
Minimum Operations
Learning Dynamic programming
"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    checker issues
    """
    if n <= 1:
        return 0

    dp: int = 0
    count: int = 2
    while (count <= n):
        if not (n % count):
            n = int(n / count)
            dp += count
            count = 1
        count += 1
    return dp
