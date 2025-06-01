#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """Represents the base class for geometry-related operations"""

    def area(self):
        """Error indicatin that the area method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer"""
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value
