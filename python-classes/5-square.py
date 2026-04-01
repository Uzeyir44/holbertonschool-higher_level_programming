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
        my_print (void): prints the square

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

    @property
    def size(self):
        """
        This function returns the size attribute

        Returns:
            int: the value of size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        This function sets a new value for size attribute

        Args:
            value (int): new size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0

        """

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        This function returns the area of the square

        Returns:
            int: the value of area
        """

        return (self.__size**2)

    def my_print(self):
        """
        This function prints the square with # characters
        """
        if (self.__size == 0):
            print("")

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
