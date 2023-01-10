#!/usr/bin/python3

"""This module defines the class_to_json function"""


def class_to_json(obj):
    """get the dictionary description of an object.

    Args:
        obj: an instance of a class

    """
    return vars(obj)
