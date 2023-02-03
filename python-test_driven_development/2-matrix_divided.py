#!/usr/bin/python3
""" module documentation """


def matrix_divided(matrix, div):
    """ matrix division function """

    if not all(isinstance(el, list) for el in matrix):
        raise\
                TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in list] for list in matrix]
