#!/usr/bin/python3
"""
This module contains class Square
"""


class Square(object):
    """
    This class represents a square

    Args:
        object (_type_): superclass with basic commands

    Attributes:
        size (int): private instance, the length of square

    Methods:
        area (int): returns the area of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        This function returns the area of the square

        Returns:
            int: the value of area
        """

        return (self.__size**2)
