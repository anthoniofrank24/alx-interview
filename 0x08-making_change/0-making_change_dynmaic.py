#!/usr/bin/python3
"""
This module contains the makeChange function to determine the fewest
number of coins needed to meet a given total amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Args:
        coins (list of int): A list of the values of
            the coins in your possession.
        total (int): The total amount to be met.

    Returns:
        int: Fewest number of coins needed to meet the total,
        or -1 if the total
        cannot be met by any number of coins you have.
    """
    if total <= 0:
        return 0

    # Initialize DP array with a large number (total + 1)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
