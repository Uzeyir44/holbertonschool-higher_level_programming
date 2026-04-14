#!/usr/bin/python3
"""
This module contains read_file function
"""


def read_file(filename=""):
    """
    This function reads a given file and prints it

    Args:
        filename (str, optional): a path to the file. Defaults to "".
    """
    with open(filename, encoding="utf-8") as afile:
        print(afile.read(), end="")
