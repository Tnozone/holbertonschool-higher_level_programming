#!/usr/bin/python3
""" module documentation """


def print_square(size):
    """ print square function """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size is < 0:
        raise TypeError("size must be an integer")

    for x in size:
        for y in size:
            print("#")
        print()
