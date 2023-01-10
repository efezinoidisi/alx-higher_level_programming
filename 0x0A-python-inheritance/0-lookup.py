#!/usr/bin/python3

"""
This is the 0-lookup module.

This module supplies one function, lookup().

"""


def lookup(obj):
    """
    This function returns a list of avalaible attribures and
    methods of an object.

    Args:
       obj: object

    Return:
          list of object attributes and functions
    """
    return dir(obj)
