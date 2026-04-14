#!/usr/bin/python3
"""
This module contains write_file function
"""


def write_file(filename="", text=""):
    """
    This function overwrites file with a new text

    Args:
        filename (str, optional): file to be ovewritten. Defaults to "".
        text (str, optional): new text. Defaults to "".

    Returns:
        int: the number of written characters
    """
    with open(filename, mode="w", encoding="utf-8") as afile:
        afile.write(text)
        return (len(text))
