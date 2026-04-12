#!/usr/bin/python3
"""
This module contains inherits_from function
"""


def inherits_from(obj, a_class):
    """
    This function checks if a class of an instance
    is inherited from given class

    Args:
        obj (_type_): instance of any class
        a_class (_type_): partcicular class

    Returns:
        bool: True if class is subclass, False in opposite
    """
    return (issubclass(type(obj), a_class))
