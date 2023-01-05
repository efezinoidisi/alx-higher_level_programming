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

        self.__size = size

    def __eq__(self, other):
        area_self = self.area()
        area_other = other.area()
        return area_self == area_other

    def __ne__(self, other):
        area_self = self.area()
        area_other = other.area()
        return area_self != area_other

    def __lt__(self, other):
        area_self = self.area()
        area_other = other.area()
        return area_self < area_other

    def __le__(self, other):
        area_self = self.area()
        area_other = other.area()
        return area_self <= area_other

    def __gt__(self, other):
        area_self = self.area()
        area_other = other.area()
        return area_self > area_other

    def __ge__(self, other):
        area_self = self.area()
        area_other = other.area()
        return area_self >= area_other

    @property
    def size(self):
        """ This is the size property

        if this value is less than zero, it raises a value exception,
        if it's not an integer, it raises a type exception
        """
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get the area of the square

           Returns:
               the area of the square
        """

        return self.__size**2
