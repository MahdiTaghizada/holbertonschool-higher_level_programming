#!/usr/bin/python3
"""This module defines a function that adds two integers.
The function ensures the arguments are integers or floats,
casts floats to integers before addition, and raises
appropriate exceptions when needed.
"""


def add_integer(a, b=98):
    """Add two integers or floats and return the result as an integer.

    Args:
        a (int or float): first number
        b (int or float, optional): second number (default = 98)

    Returns:
        int: the sum of a and b after casting to integers.

    Raises:
        TypeError: if a or b are not integers or floats
        OverflowError: if a or b are NaN or infinity
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num):
    """Convert a float to an int, checking for NaN or infinity."""
    if type(num) is float:
        # check NaN (NaN != NaN)
        if num != num:
            raise OverflowError("cannot convert float NaN to integer")
        # check infinity (+inf or -inf)
        if num == float("inf") or num == float("-inf"):
            raise OverflowError("cannot convert float infinity to integer")
        num = int(num)
    return num
