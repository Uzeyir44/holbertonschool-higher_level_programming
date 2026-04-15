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
    def __init_(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This function creates a dictionary of instance's attributes

        Return:
            (dict): dictionary of the attributes
        """
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name
            "age" : self.age
        }
