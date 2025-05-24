#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with a width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
