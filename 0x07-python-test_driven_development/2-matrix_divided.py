#!/usr/bin/python3
"""
Create a function that divides all
elements of a matrix
implemented python test
"""


def matrix_divided(matrix, div):
    """
    matrix division funtion
    two args:
    matrix = list
    div = integers
    """

    ErrorMessage = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(ErrorMessage)

    matrix_new = []
    for matrix_row in matrix:
        if len(matrix_row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        
        if type(matrix_row) is not list:
            raise TypeError(ErrorMessage)
        
        row = []
        for n in matrix_row:
            if type(n) not in [int, float]:
                raise TypeError(ErrorMessage)

            row += [round(n / div, 2)]
        matrix_new += [row]
    return matrix_new
        
