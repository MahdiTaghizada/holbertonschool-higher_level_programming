#!/usr/bin/python3
"""A module to add two numbers"""


def add_integer(a, b=98):
    """Adds two numbers"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num):
    """Convert a float to int safely"""
    if type(num) is float:
        if num != num or num == float("inf") or num == float("-inf"):
            raise OverflowError("cannot convert float NaN to integer")
        num = int(num)
    return num
