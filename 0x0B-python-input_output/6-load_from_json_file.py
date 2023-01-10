#!/usr/bin/python3

"""This module defines the load_feom_json_file function"""
from json import load


def load_from_json_file(filename):
    """creates an object fro a json file.

    Args:
        filename: name of file

    """
    with open(filename, 'r', encoding='utf-8') as f:
        return load(f)
