#!/usr/bin/python3
"""
This module contains Fish, Bird and FlyingFish classes
"""


class Fish:
    """
    This class describes a fish
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    This class describes a bird
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    This class describes a flying fish

    Args:
        Fish: parent class
        Bird: parent class
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print( "The flying fish lives both in water and the sky!")
