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

    def area(self):
        """Calculate and return the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def my_print(self):
        """Print the rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Define the string representation of the rectangle to print"""

        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Define the official representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
