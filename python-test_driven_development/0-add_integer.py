#!/usr/bin/python3
"""A module to add two numbers"""


def add_integer(a, b=98):
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num):
    if type(num) is float:
        # NaN yoxlaması
        if num != num:
            raise OverflowError("cannot convert float NaN to integer")
        # Sonsuzluq yoxlaması
        if num == float("inf") or num == float("-inf"):
            raise OverflowError("cannot convert float infinity to integer")
        num = int(num)
    return num
