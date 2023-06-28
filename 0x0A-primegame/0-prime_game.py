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

    def get_next_prime(start):
        """
        Finds the next prime number greater than the given number.

        Args:
            start (int): The starting number.

        Returns:
            int: The next prime number greater than 'start'.
        """
        num = start + 1
        while not is_prime(num):
            num += 1
        return num

    def game_winner(n):
        """
        Determines the winner of a single round of the game.

        Args:
            n (int): The value of 'n' for the current round.

        Returns:
            str: The name of the player who wins the round.
            Returns 'Maria' or 'Ben'.
        """
        prime = 2
        while prime <= n:
            if n % prime == 0:
                n -= prime
                prime = get_next_prime(prime)
            else:
                prime = get_next_prime(prime)
        return "Maria" if n % 2 == 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
