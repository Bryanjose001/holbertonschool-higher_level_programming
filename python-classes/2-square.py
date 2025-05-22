#!/usr/bin/python3
"""Square class!"""


class Square:
    """Square class with private class attribute"""

    def __init__(self, size=0):
        """Initialize a square with size validation!"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square!"""
        return self.__size ** 2
