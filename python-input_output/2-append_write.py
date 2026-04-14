#!/usr/bin/python3
"""
This module contains append_write function
"""


def append_write(filename="", text=""):
    """
    This function appends new text to the file

    Args:
        filename (str, optional): path to the file. Defaults to "".
        text (str, optional): text to be added. Defaults to "".

    Returns:
        int: the number of added characters
    """
    with open(filename, mode="a", encoding="utf-8") as afile:
        afile.write(text)
        return (len(text))
