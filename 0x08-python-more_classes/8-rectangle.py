#!/usr/bin/python3

""" This module defines a Rectangle class """


class Rectangle:
    """This is a Rectangle class with a width and height

    Attributes:
         number_of_instances (int): number of instances of the Rectangle class
         print_symbol (any): used as a symbol for string representation

    Args:
           width (int): width of the rectangle
           height (int): height of the rectangle


    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """ Prints the rectangle using the character '#'"""

        rectangle = ""

        if not self.width or not self.height:
            return rectangle

        for i in range(self.height):
            for x in range(self.width):
                rectangle += str(self.print_symbol)
            if i != self.height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """This gives the string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ This method is called whenever an instance is deleted"""
        type(self).number_of_instances -= 1
        print(f"Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ This method checks for the bigger rectangle based on
        the area of the rectangles given

        Returns:
            The biggest rectangle

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()
        if rect_1_area == rect_2_area:
            return rect_1
        elif rect_1_area > rect_2_area:
            return rect_1
        else:
            return rect_2
