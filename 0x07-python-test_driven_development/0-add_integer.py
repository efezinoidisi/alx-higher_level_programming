#!/usr/bin/python3

"""
 This is the 0-add_integer module.
 
 This module supplies one function, add_integer(). e.g

 >>> add_integer(7, 1)
 8
"""


def add_integer(a, b=98):
    """Add two integers

    Args:
       a (int): first number to be added
       b (int): second number to be added

    Returns:
        the sum of a and b

    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
