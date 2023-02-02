#!/usr/bin/python3
""" module documentation """


def add_integer(a, b=98):
    """ addition function """

    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
