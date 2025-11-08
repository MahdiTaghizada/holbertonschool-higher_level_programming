#!/usr/bin/python3
"""This module contains a Square class."""


class Square():
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class"""
        self.size = size
        self.position = position

    def area(self):
        """Function that computes the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter for size"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """Setter for size"""
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Prints square"""
        if (self.size == 0):
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

    @property
    def position(self):
        """Getter for position"""
        return (self.__position)

    @position.setter
    def position(self, p):
        """Setter for position"""
        if (not isinstance(p, tuple) or
                len(p) != 2 or
                not (isinstance(p[0], int) and isinstance(p[1], int)) or
                not (p[0] >= 0 and p[1] >= 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = p
