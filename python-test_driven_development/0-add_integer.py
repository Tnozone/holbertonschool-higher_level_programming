#!/usr/bin/python3
""" module documentation """


def add_integer(a, b=98):
    """ addition function """

    if a is not int or a is not float:
        raise TypeError("a must be an integer")
    elif b is not int or b is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
