#!/usr/bin/python3
""" module documentation """


class MyList(list):
    """ class inherits list """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
