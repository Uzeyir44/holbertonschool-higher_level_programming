#!/usr/bin/python3
"""
This module contains BaseGeometry class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This array inherits from Rectangle and describes square

    Args:
        Rectangle (Rectangle): base class

    Attributes:
        __size (int): value of the side
    """
    def __init__(self, size):
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        This function finds the area of square

        Returns:
            int: the value of the area
        """
        return (self.__size**2)
