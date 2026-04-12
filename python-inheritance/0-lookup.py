#!/usr/bin/python3
"""
This module contains a lookup function
"""


def lookup(object):
    """
    This function prints all attributes of a given class

    Arguments:
        object (class): a particular class

    Return:
        (list): returns a list of class attributes
    """
    return (dir(object))
