#!/usr/bin/python3
"""
This module contains is_same_class function
"""


def is_same_class(obj, a_class):
    """
    This class checks if object is an instance
    of given class

    Args:
        obj (_type_): an anstance of a some class
        a_class (_type_): a particular class

    Returns:
        (bool): True if instance is from this class, False if
        opposite
    """
    return (isinstance(obj, a_class))
