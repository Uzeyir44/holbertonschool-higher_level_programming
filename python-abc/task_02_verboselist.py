#!/usr/bin/python3
"""
This module contains VerboseList class
"""


class VerboseList(list):
    """
    This class is an extended version of list class

    Args:
        list : parent class
    """
    def append(self, item):
        """
        This function overwrites append function

        Args:
            item (void): item appended to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """
        This function overwrites extend function

        Args:
            item (list): list appended to the list
        """
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """
        This function overwrites remove function

        Args:
            item (void): item removed from the list
        """
        super().remove(item)
        print(f"Removed [{item}] from the list")

    def pop(self, item=-1):
        """
        This function overwrites pop function

        Args:
            item (int): index of a removed element
        """
        value = super().pop(item)
        print(f"Popped [{value}] from the list")
        return value
