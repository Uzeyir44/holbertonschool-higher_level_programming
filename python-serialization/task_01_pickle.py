#!/usr/bin/python3
"""
This module contains CustomObject class
"""

import pickle


class CustomObject:
    """
    This class describes an object

    Attrs:
        name (string): name of the string
        age (int): age of the object
        is_student (bool): status of the object

    Methods:
        display: prints all attributes of object
        serialize: serializes instace and saves it in file
        deserialize: creates new instance with data in file
    """

    def __init__(self, name:str, age:int, is_student:bool):
        """
        inside the init file
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        This function prints the attributes of class instances
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        This function serializes instace and saves it in file

        Args:
            filename: path to the file
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        This function creates new instance with data in file

        Args:
            filename: path to the file
        """
        with open(filename, 'rb') as file:
            try:
                deserialized_list = pickle.load(file)
                return deserialized_list
            except Exception:
                pass
