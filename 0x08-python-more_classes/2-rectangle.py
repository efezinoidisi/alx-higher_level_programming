#!/usr/bin/python3

""" This module defines a Rectangle class """


class Rectangle:
    """This is a Rectangle class with a width and height

    Args:
           width (int): width of the rectangle
           height (int): height of the rectangle


    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ This is the width property

        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This property defines the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This method calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ This method calculates the perimeter of the rectangle"""
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)
