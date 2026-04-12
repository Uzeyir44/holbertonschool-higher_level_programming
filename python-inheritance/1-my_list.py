#!/usr/bin/python3
"""
This module contains class MyList
"""


class MyList(list):
    """
    This class is a subcalss of list class

    Args:
        list (list): built-in class list

    Methods:
        print_sorted: prints the sorted version of instance
    """
    def print_sorted(self):
        """
        This function prints a sorted version od argument
        """
        temp = self[:]
        temp.sort()
        print(temp)
