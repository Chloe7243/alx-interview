#!/usr/bin/python3
""" 0x0A. Prime Game """


def isPrimeNumber(n):
    """Checks If Number Is Prime"""
    isPrime = True
    i = 2
    while i <= n / 2:
        if n % i == 0:
            isPrime = False
            break
        i += 1
    return isPrime


def getNoPrimeNumbers(n):
    """Gets Number of prime numbers between 2 and n"""
    i = 2
    noPrimeNumbers = 0
    while i <= n:
        if isPrimeNumber(i):
            noPrimeNumbers += 1
        i += 1
    return noPrimeNumbers


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
