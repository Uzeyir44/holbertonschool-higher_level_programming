#!/usr/bin/python3
"""
This module contains BaseGeometry class
"""


class BaseGeometry:
    """
    A geometry class

    Methods:
        area: raises an exception
        integer_validator: checks if the argument is integer
    """
    def area(self):
        """
        Raises an exception

        Raises:
            Exception: just raises this exception always
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function raises exceptions based on the value
        of the second argument

        Args:
            name (string): name
            value (int): the value of the name

        Raises:
            TypeError: if value is not int
            ValueError: if value <= 0
        """
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
