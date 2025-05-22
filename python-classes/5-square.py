#!/usr/bin/python3
"""This module defines a Square class for representing squares."""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square's sides (must be >= 0).
    """

    def __init__(self, size=0):
        """Initializes a Square instance with size validation.

        Args:
            size (int, optional):
            The size of the square's sides, Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for the size attribute.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square using the '#' character based on its size.

        If the size is 0, an empty line is printed. Otherwise, the square
        is printed with the side length corresponding to the size attribute.
        """
        if self.__size != 0:
            for index in range(self.__size):
                for innerindex in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
