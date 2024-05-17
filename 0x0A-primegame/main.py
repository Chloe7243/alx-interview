#!/usr/bin/env python3

isWinner = __import__("0-prime_game").isWinner


print("Winner: {}".format(isWinner(10000, list(range(1, 10001)))))
