from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Concrete class representing a circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return (math.pi * self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the cirlce"""
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """Concrete class representing a rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return (2 * (self.width + self.height))


def shape_info(shape):
    """print the area and perimeter of a shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
