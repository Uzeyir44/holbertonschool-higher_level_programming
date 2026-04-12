#!/usr/bin/python3
"""
This module contains BaseGeometry class
"""


class BaseGeometry:
    """
    A geometry class

    Methods:
        area: raises an exception
    """
    def area(self):
        """
        Raises an exception

        Raises:
            Exception: just raises this exception always
        """
        raise Exception("area() is not implemented")
