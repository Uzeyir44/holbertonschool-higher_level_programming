#!/usr/bin/python3
"""
This module contains Dragon, SwimMixin and FlyMixin calsses
"""


class SwimMixin:
    """
    This class has swiming behaviour
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    This class has flying behaviour
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    This class describes dragon

    Args:
        SwimMixin: mixin class
        FlyMixin: mixin class
    """
    def roar(self):
        print("The dragon roars!")
