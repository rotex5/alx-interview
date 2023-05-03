#!/usr/bin/python3
"""
Minimum Operations
Learning Dynamic programming
"""
# from typing import Union


def minOperations(n: int) -> int:
    if n < 1:
        return 0

    # Initialize a list to store the minimum number
    # of operations required for each state
    # We start with the initial state (1 H character)
    # and compute subsequent states until n
    dp = [0] + [float('inf')] * (n - 1)

    for i in range(2, n + 1):
        # If i is a prime number, we cannot reach this
        # state by copying and pasting
        if is_prime(i):
            continue

        # Find the minimum number of operations
        # required to reach state i
        for j in range(i - 1, 0, -1):
            if i % j == 0:
                dp[i - 1] = min(dp[i - 1], dp[j - 1] + i // j)

    return dp[-1]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
