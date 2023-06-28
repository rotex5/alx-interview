#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of each game played.

    Args:
      x (int): The number of rounds.
      nums (list): An array of n for each round.

    Returns:
      str: Name of the player who won the most rounds.
           If the winner cannot be determined, returns None.
    """
    if not nums or x < 1:
        return None

    wins = 0

    for n in nums:
        primes = c_primes(n)
        if primes % 2 == 1:
            wins += 1

    if wins % 2 == 0:
        return "Ben"
    return "Maria"


def c_primes(n):
    """
    Counts the number of prime numbers up to and including n.

    Args:
      n (int): The upper limit.

    Returns:
      int: The count of prime numbers.
    """
    if n < 2:
        return 0

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return sum(primes)


def prime_num(num):
    """
    Checks if a number is prime.

    Args:
      num (int): The number to check.

    Returns:
      bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
