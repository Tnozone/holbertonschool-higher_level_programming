#!/usr/bin/python3
""" class module documentation """


class Square:
    """ Square class with private instance attribute size """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        self.area = size ** 2
