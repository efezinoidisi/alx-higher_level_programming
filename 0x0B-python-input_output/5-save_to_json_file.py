#!/usr/bin/python3

"""This module defines the save_to_json_file function"""
from json import dump


def save_to_json_file(my_obj, filename):
    """get json representation of an object and save to a text file.

    Args:
        my_obj: object
        filename: name of file

    """
    with open(filename, 'w', encoding='utf-8') as f:
        dump(my_obj, f)
