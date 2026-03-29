#!/usr/bin/python3
"""
This module contains a function that prints a square
"""


def print_square(size):
    """
    Prints a square

    Args:
        size (int): the length and width of square
        
    Return:
        Does not return any value
        
    Raise:
        TypeError: if size is not an int or if its float and less then 0
        ValueError: if size < 0
    """
    if ((type(size) is float and size < 0) or type(size) is not int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
