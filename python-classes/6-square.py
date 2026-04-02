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
        position (tuple): the coordinates of square

    Methods:
        area (int): returns the area of the square
        my_print (void): prints the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """

    def __init__(self, size=0, position=(0, 0)):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if (type(position) is not tuple
                or len(position) != 2
                or not all(isinstance(n, int) and n >= 0 for n in position)):
            # This comment provides visual distinction
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        This function returns the position attribute

        Returns:
            tuple: the value of position
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """
        This function sets a new value for position attribute

        Args:
            value (tuple): new coordinates

        Raises:
            TypeError: if value is not a tuple and
            its elements are not positive integers
        """

        if (type(value) is not tuple
                or len(value) != 2
                or not all(isinstance(n, int) and n >= 0 for n in value)):
            # This comment provides visual distinction
            raise TypeError("position must be a tuple of 2 positive integers")

        self._position = value

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
            return

        for k in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
