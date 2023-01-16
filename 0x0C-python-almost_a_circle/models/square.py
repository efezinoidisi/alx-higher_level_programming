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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
         size of the square: which is the width or height of a
            rectangle
         """
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value

    def update(self, *args, **kwargs):
        if args:
            try:

                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        elif kwargs:
            keys = kwargs.keys()
            if 'id' in keys:
                self.id = kwargs['id']
            if 'size' in keys:
                self.size = kwargs['size']
            if 'x' in keys:
                self.x = kwargs['x']
            if 'y' in keys:
                self.y = kwargs['y']
