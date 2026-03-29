#!/usr/bin/python3
"""
This module contains function that prints first and last name of user    
"""


def say_my_name(first_name, last_name=""):
    """
    Prints lastname and firstname od user

    Args:
        first_name (str): firstname
        last_name (str): lastname. Defaults to "".

    Return:
        Does not return any value

    Raises:
        TypeError: if first_name or last_name are not strings
    """

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
