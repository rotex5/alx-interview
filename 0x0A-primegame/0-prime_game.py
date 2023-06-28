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
    players = {'Maria': 0, 'Ben': 0}
    cluster = set()
    for elem in range(x):
        nums.sort()
        num = nums[elem]
        for i in range(1, num + 1):
            cluster.add(i)
            if i == num + 1:
                break
        temp = count_primes(cluster)

        if temp % 2 == 0:
            players['Ben'] += 1
        elif temp % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None


def is_prime(num):
    """
    Checks if a given number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def remove_multiples(num, lst):
    """
    Removes multiples of a given number from a list
    """
    new_lst = [item for item in lst if item % num != 0]
    return new_lst


def count_primes(nums):
    """
    Counts the number of primes in a given set
    """
    counter = 0
    target = list(nums)
    for i in range(1, len(target) + 1):
        if is_prime(i):
            counter += 1
            target = remove_multiples(i, target)
    return counter
