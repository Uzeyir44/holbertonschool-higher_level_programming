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

    Methods:
        area (int): returns the area
        perimeter (int): returns the perimeter
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

    def area(self):
        """
        This function evaluates the area of rectangle

        Return:
            (int): the product of height and width
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        This function evaluates the perimeter of rectangle

        Return:
            (int): the double sum of height and width
        """
        if (self.__height == 0 or self.__width == 0):
            return (0)

        return (2 * (self.__width + self.__height))

    def __str__(self):
        if (self.__height == 0 or self.__width == 0):
            return ("")
        for i in range(self.__height):
            print("#" * self.__width)

    def __repr__(self):
        print(f"Rectangle({self.__width}, {self.__height})")
