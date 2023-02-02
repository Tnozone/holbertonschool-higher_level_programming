#!/usr/bin/python3
""" module documentation """


def matrix_divided(matrix, div):
    """ matrix division function """

    return [[round(x / div, 2) for x in list] for list in matrix]
