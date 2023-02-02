#!/usr/bin/python3
""" module documentation """


def add_integer(a, b=98):
    """ addition function """

    if a is not isinstance(a, int) or a is not isinstance(a, float):
        raise TypeError("a must be an integer")
    if b is not isinstance(b, int) or b is not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
