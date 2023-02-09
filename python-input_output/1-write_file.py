#!/usr/bin/python3
""" Class Module """


def write_file(filename="", text=""):
    """ read file function """

    with open(filename, "w") as f:
        f.write(text)
        return len(text)
