#!/usr/bin/python3

"""This module defines the to_json_string function"""
from json import dumps


def to_json_string(my_obj):
    """get json representation of an object

    Args:
        my_obj: object

    Return:
        the json representation

    """
    return dumps(my_obj)
