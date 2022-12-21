#!/usr/bin/python3
"""This module defines a class called Square.
"""


class Square:
    """This defines a square class with a private
       instance attribute size


    Args:
        size (int): size of the square
        position (tuple): x and y coordinates of the square

    """
    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ This is the position property
            if this value is not a tuple of 2 integers,
            raise a type exception
        """
        return self.__position

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

    def area(self):
        """Get the area of the square

           Returns:
               the area of the square
        """

        return self.__size**2

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
