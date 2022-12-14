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

        self.size = size
        self.position = position

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
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get the area of the square

           Returns:
               the area of the square
        """

        return self.size**2

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for i in range(self.size):
                for _ in range(self.position[0]):
                    print(" ", end="")
                for _ in range(self.size):
                    print("#", end="")
                print()
