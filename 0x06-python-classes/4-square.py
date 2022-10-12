#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Define a class Square."""

    def __init__(self, size=0):
        """ Initialize method.
        Args:
            self (class): This class
            size (int): Size of the square
        """

        """ Instance attribute
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size**2
