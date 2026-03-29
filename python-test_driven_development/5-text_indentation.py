#!/usr/bin/python3
"""
This module contins a function that replases .? and : with two new lines
"""


def text_indentation(text):
    """
    Prints each sentence in a new line

    Args:
        text (string): the original text

    Return:
        Does not return any value

    Raise:
        TypeError: if text is not str
    """
    if (type(text) is not str):
        raise TypeError("text must be a string")

    flag = False
    for i in text:
        if (flag):
            flag = False
            continue

        if (i == "." or i =="?" or i==":"):
            print("{}\n".format(i))
            flag = True
        else:
            print("{}".format(i), end="")
    print("")
