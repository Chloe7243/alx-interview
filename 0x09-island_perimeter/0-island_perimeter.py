#!/usr/bin/python3
"""
Program that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    island_perimeter
    """
    perimeter = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or row[j - 1] == 0:
                    perimeter += 1
                if j + 1 == len(row) or row[j + 1] == 0:
                    perimeter += 1
                if i + 1 == len(grid) or grid[i + 1][j] == 0:
                    perimeter += 1
    return perimeter


grid = [[1, 0]]
print(island_perimeter(grid))
