#!/usr/bin/env python3
""" Given an n x n 2D matrix, rotate it 90 degrees clockwise. """


def rotate_2d_matrix(matrix):
    matrix_len = len(matrix)
    rotated_matrix = []
    for i, row in enumerate(matrix):
        rotated_matrix.append([])
        for j, val in enumerate(row):
            rotated_matrix[i].append([])
            rotated_matrix[i][j] = matrix[matrix_len - (j + 1)][i]

    for i, row in enumerate(rotated_matrix):
        matrix[i] = row
