#!/usr/bin/python3
""" Class Module """


def append_write(filename="", text=""):
    """ append function """

    with open(filename, "a") as f:
        f = f.write(text)
        return len(text)
