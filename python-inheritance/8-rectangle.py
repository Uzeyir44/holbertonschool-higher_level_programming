#!/usr/bin/python3
"""
This module contains BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class is a subclass of BaseGeometry and describes
    rectangles

    Args:
        BaseGeometry (BaseGeometry): a parent class

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__height = height
        self.__width = width
