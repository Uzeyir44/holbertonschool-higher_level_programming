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
    """

    def __init__(self, size):
        self.__size = size
