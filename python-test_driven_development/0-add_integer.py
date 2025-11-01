#!/usr/bin/python3
"""A module to add two numbers"""


def add_integer(a, b=98):
    """Adds two integers or floats (after casting to int)"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Handle NaN or infinity manually (since we can't import math)
    if a != a or b != b:  # NaN check (NaN != NaN is always True)
        raise OverflowError("cannot convert float NaN to integer")
    if a == float('inf') or a == float('-inf') or \
       b == float('inf') or b == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
