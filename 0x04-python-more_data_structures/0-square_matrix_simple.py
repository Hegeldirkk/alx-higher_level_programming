#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for n in range(0, 3):
        new_matrix[n] = list(map(lambda x: x*x, new_matrix[n]))
    return new_matrix
