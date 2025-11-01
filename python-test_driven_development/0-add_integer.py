#!/usr/bin/python3
"""A module to add two numbers"""


def add_integer(a, b=98):
    """Add two integers or floats and return the result as an integer.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The integer sum of a and b.

    Raises:
        TypeError: If either a or b is not an int or float.
        OverflowError: If a or b is NaN or infinity.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num):
    """Convert a float to int safely."""
    if type(num) is float:
        if num != num:
            raise OverflowError("cannot convert float NaN to integer")
        if num == float("inf") or num == float("-inf"):
            raise OverflowError("cannot convert float infinity to integer")
        num = int(num)
    return num
