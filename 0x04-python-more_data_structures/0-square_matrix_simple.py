#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for n in matrix:
        resultat = list(map(lambda x: x**2, n))
        new_matrix.append(resultat)
    return new_matrix
