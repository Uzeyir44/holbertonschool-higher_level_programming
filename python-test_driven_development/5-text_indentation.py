#!/usr/bin/python3
"""
This module contins a function that replases .? and : with two new lines
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'

    Args:
        text (str): input text

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]

        if char in ".?:":
            print(char)
            print()
            i += 1
            # skip spaces after punctuation
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(char, end="")
            i += 1
