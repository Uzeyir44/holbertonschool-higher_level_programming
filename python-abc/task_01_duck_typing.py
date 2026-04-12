#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
This module contains abstract class Shape, Circle and Rectangle classes
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    This class describes circle

    Args:
        Shape: parent class
    
    Methods:
        area: returns the area of instance
        perimeter: returns the perimeter of instance
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Finds the area of object

        Returns:
            int: the area of object
        """
        return (pi * self.radius**2)

    def perimeter(self):
        """
        Finds the perimeter of object

        Returns:
            int: the perimeter of object
        """
        return (2 * pi * self.radius)


class Rectangle(Shape):
    """
    Describes the rectangle

    Args:
        Shape: parent class
    
    Methods:
        area: returns the area of instance
        perimeter: returns the perimeter of instance
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Finds the area of object

        Returns:
            int: the area of object
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Finds the perimeter of object

        Returns:
            int: the perimeter of object
        """
        return ((self.width + self.height) * 2)


def shape_info(obj):
    """
    This function calls the methods of functions

    Args:
        obj : any subclass of Shape
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
