#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
This module contains abstract class animal, Dog and Cat subclass
"""


class Animal(ABC):
    """
    An abstract class

    Args:
        ABC : an abstract class definer
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    A class that describes a dog

    Args:
        Animal: parent class for dog
    """
    def sound(self):
        """
        This function returns dog's sound

        Returns:
            string: dog's sound
        """
        return ("Bark")


class Cat(Animal):
    """
    This class describes cat

    Args:
        Animal: parent class for this class
    """
    def sound(self):
        """
        This function returns a cat's sound

        Returns:
            string: returns cat's sound
        """
        return ("Meow")
