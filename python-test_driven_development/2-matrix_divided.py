#!/usr/bin/python3
""" module documentation """

def matrix_divided(matrix, div):
    """ matrix division function """

    new = matrix[:]
    for i in matrix:
        new[i] = matrix[i] / div
    return new
