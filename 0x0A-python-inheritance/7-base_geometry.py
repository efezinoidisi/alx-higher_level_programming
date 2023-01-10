#!/usr/bin/python3
"""
This module defines the BaseGeometry class

"""


class BaseGeometry():
    """

    A class that defines the Base Geometry

    """
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
