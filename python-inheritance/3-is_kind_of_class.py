#!/usr/bin/python3
"""
This module contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if object is instance of a class
    or instance of its base class

    Args:
        obj (_type_): object of any class
        a_class (_type_): particular class

    Returns:
        bool: True if instance is from this class ot its parent,
        False if opposite
    """
    return (isinstance(obj, a_class))
