#!/usr/bin/python3
"""
    Define a class
"""


class Rectangle:
    """ Rectangle Class """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ return width """

        return self.__width

    @width.setter
    def width(self, value):
        """ Check values """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return height """

        return self.__height

    @height.setter
    def height(self, value):
        """ Check values """

        is not isinstance(value, int):
            raise TypeError("height must be an integer")
        is value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
