#!/usr/bin/python3
"""This module defines a Square class for representing squares."""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square's sides (must be >= 0).
        __position (tuple): The position of the square
        (tuple of 2 positive integers).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with size and position validation.

        Args:
            size (int, optional): The size of the square's sides.
            Defaults to 0.
            position (tuple of 2 positive integers, optional):
            The position to start printing the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute with validation.

        Args:
            value (tuple): The position of the square as a
            tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        error = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(error)
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError(error)
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square using the '#' character
        based on its size and position.

        If the size is 0, an empty line is printed. Otherwise,
        the square is printed
        with the side length corresponding to the size attribute and
        offset by the position.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
