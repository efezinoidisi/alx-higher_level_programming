#!/usr/bin/python3
"""
This module contains the class Square

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits from the Rectangle class.

    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor method for the Square class.

        Args:
             id (int): id of each instance
             width: width of the rectangle
             height: height of the rectangle
             x: x coordinates
             y: y coordinates

        """
        super().__init__(size, size, x, y, id)

        def __str__(self):
            return f"[Square] (self.id) {self.x}/{self.y} - {self.size}"

        @property
        def size(self):
            return self.width

        @size.setter
        def size(self, value):
            self.width = self.height = value
