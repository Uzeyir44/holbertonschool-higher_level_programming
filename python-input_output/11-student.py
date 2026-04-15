#!/usr/bin/python3
"""
This module contains Student class
"""


class Student:
    """
    This class describes Student

    Attributes:
        first_name (string): the name of student
        last_name (string): the last name of student
        age (int): the age of the student

    Methods:
        to_json: returns the library of instances attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function creates a dictionary of instance's attributes

        Return:
            (dict): dictionary of the attributes
        """
        dct = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        if (attrs is None):
            return (dct)
        new_dct = {}
        for i in attrs:
            if i in dct.keys():
                new_dct[i] = dct[i]
        return (new_dct)
    def reload_from_json(self, json):
        """
        This function changes all attributes of instance
        to the new ones

        Args:
            json (dict): dictionary with new values for instance
        """
        if json:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
