#!/usr/bin/python3
"""
This module contains CountedIterator class
"""


class CountedIterator:
    """
    This class describes iterator
    """
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        This function returns the count attribute

        Returns:
            int: retunrs current value of count attribute
        """
        return (self.count)

    def __next__(self):
        value = next(self.iterator)
        self.count += 1
        return (value)

    def __iter__(self):
        return self
