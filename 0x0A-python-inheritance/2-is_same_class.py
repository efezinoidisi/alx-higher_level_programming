#!/usr/bin/python3

"""
This is the 2-is_same_class module.

This module supplies one function, is_same_class().

"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
       obj: an object
       a_class: class to check

    Return:
          True or False
    """
    if type(obj) == a_class:
        return True
    return False
