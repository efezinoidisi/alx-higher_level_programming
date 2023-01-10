#!/usr/bin/python3

"""
This is the 3-is_kind_of_class module.

This module supplies one function, is_kind_of_class().

"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class
    or of a class inherited from the specified class.

    Args:
       obj: an object
       a_class: class to check

    Return:
          True or False
    """
    return isinstance(obj, a_class)
