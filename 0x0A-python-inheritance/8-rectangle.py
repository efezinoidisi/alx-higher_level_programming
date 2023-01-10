#!/usr/bin/python3
"""
This module defines the Rectangle class

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """

    A class that defines a Rectangle that inherits from
    the Base Geometry class

    Args:
        width (int): width of rectangle
        height (int): height of rectangle

    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
