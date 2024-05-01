#!/usr/bin/env python3
"""
Main file for testing
"""

makeChange = __import__("0-making_change").makeChange

print( 1, makeChange([1, 2, 25], 37))
print( 2, makeChange([1256, 54, 48, 16, 102], 1453))
print( 3, makeChange([], 10))  # Empty list of coins
print( 4, makeChange([1, 2, 3], 0))  # Total of 0
print( 5, makeChange([1, 2, 3], -5))  # Negative total
print( 6, makeChange([5, 10, 20], 7))  # Total cannot be met
print( 7, makeChange([10], 10))  # Single coin value equal to total
print( 8, makeChange([100], 50))  # Single coin value larger than total
print( 9, makeChange([1, 5, 10, 25], 47))  # Multiple coins needed
print( 10, makeChange([1, 2, 5, 10, 20, 50, 100], 150))  # Large total
print( 11, makeChange([1, 2, 5, 10, 20, 50, 100], 1000))  # Large total
print( 12, makeChange([1, 2, 5, 10, 20, 50, 100], 9999))  # Large total
print( 13, makeChange([1, 2, 5, 10, 20, 50, 100], 100000))  # Large total
print( 14, makeChange([1, 2, 5, 10, 20, 50, 100], 1000000))  # Large total
