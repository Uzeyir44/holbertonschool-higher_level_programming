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
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        This function prints the attributes of class instances
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        This function serializes instace and saves it in file

        Args:
            filename: path to the file
        """
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        This function creates new instance with data in file

        Args:
            filename: path to the file
        """
        with open(filename, mode="rb") as file:
            return (pickle.load(file))
