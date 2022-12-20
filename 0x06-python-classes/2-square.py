#!/usr/bin/python3
"""This module defines a class called Square.
"""


class Square:
    """This defines a square class with a private
       instance attribute size


    Args:
        size (int): size of the square


    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
