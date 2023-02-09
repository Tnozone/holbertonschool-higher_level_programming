#!/usr/bin/python3
""" Class Module """


def read_file(filename=""):
    """ read file function """

    with open(filename, "r") as f:
        f = f.read()
        print(f, end="")
