#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total.
"""
import math


def makeChange(coins, total):
    """Make change"""
    coins_needed = 0
    coins.sort(reverse=True)
    for coin in coins:
        if total > 0:
            if coin > total:
                continue
            coins_needed += math.trunc(total / coin)
            total = total % coin
        else:
            break
    return coins_needed if total == 0 else -1
