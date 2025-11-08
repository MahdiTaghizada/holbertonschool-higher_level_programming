#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the charecter #."""
        i = 0
        if self.__size == 0:
            print("")
        else:
            while i < self.__size:
                print("#" * self.__size)
                i = i + 1

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, p):
        """Setter for position"""
        if (not isinstance(p, tuple) or
                len(p) != 2 or
                not (isinstance(p[0], int) and isinstance(p[1], int)) or
                not (p[0] >= 0 and p[1] >= 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = p
