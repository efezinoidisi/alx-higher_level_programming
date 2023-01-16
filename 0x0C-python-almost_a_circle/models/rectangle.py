#!/usr/bin/python3
"""
The rectangle module contains the class Rectangle

"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class inherits from the Base class.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method for the Rectangle class.

        Args:
             id (int): id of each instance
             width: width of the rectangle
             height: height of the rectangle
             x: x coordinates
             y: y coordinates

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    @property
    def width(self):
        """
        width of the rectangle
        width must be an integer and also greater than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height of the rectangle
        height must be an integer and also greater than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x axis of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y axis of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        get the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        print the rectangle using # character

        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        update the arguments
        """

        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass
        if kwargs:
            keys = kwargs.keys()
            if 'id' in keys:
                self.id = kwargs['id']
            if 'width' in keys:
                self.width = kwargs['width']
            if 'height' in keys:
                self.height = kwargs['height']
            if 'x' in keys:
                self.x = kwargs['x']
            if 'y' in keys:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
         This method returns the dictionary representation of Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
