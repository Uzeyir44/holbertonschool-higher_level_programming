#!/usr/bin/python3
"""
This module contains class Rectangle
"""


class Rectangle:
    """
    This class represents a rectangle

    Attributes:
        width (int): private attribute representing the width
        height (int): private attribute representing the height
    """
    def __init__(self, width=0, height=0):
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        This functions serves as getter

        Return:
            self.__width (int): the width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        This function sets new value for width attribute
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        This functions serves as getter

        Return:
            self.__height (int): the width of rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        This function sets new value for height attribute
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value
