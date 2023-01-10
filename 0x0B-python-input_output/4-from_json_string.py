#!/usr/bin/python3

"""This module defines the from_json_string function"""
from json import loads


def from_json_string(my_str):
    """turn json string back to an object

    Args:
        my_str: json string

    Return:
        an object

    """
    return loads(my_str)
