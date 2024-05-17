#!/usr/bin/python3
""" 0x0A. Prime Game """


def getNoPrimeNumbers(n):
    """Gets Number of prime numbers between 2 and n"""
    i = 2
    primeNumbers = [True] * (n + 1)
    while i * i <= n:
        if primeNumbers[i] is True:
            j = i**2
            while j <= n:
                primeNumbers[j] = False
                j += i
        i += 1
    return len(list(filter(lambda x: x is True, primeNumbers))) - 2


def isWinner(x, nums):
    """Determines winner"""
    Ben = 0
    Maria = 0
    winner = None
    for i in range(x):
        noPrimeNumbers = getNoPrimeNumbers(nums[i])
        if noPrimeNumbers % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        winner = "Ben"
    elif Maria > Ben:
        winner = "Maria"
    return winner
