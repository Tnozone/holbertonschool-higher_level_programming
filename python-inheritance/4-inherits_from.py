#!/usr/bin/python3
""" Class Module """


def inherits_from(obj, a_class):
    """ inherits from function """

    return (type(obj) is not a_class and isinstance(obj, a_class))
