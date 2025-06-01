#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle"""

    def __init__(self, size):
        """Initialize width and height with validation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return super().area()

    def __str__(self):
        """Return the string representation of the square"""
        return (f"[Square] {self.__size}/{self.__size}")
