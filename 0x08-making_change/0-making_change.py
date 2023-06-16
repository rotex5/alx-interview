#!/usr/bin/python3
"""
makeChange Module
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        if coin <= total:
            # Number of coins needed for current denomination
            count = total // coin
            coin_count += count
            total -= count * coin

    if total == 0:
        return coin_count
    else:
        return -1
