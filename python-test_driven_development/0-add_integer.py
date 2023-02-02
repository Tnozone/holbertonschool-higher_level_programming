#!/usr/bin/python3
""" module documentation """


def add_integer(a, b=98):
    """ addition function """

    if a is not int and a is not float:
        raise TypeError("a must be an integer")
    elif b is not int and b is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
