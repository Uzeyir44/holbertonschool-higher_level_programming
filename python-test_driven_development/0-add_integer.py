#!/usr/bin/python3
"""
This module provides function for addition of two numbers    
"""

def add_integer(a, b=98):
    """
    Adds two numbers
    
    Args:
        a (int or float): first argument
        b (int or float): second argument
    
    Returns:
        int: result of addition
        
    Raises:
        TypeError: if a or b are not int or float
    """
    if (type(a) is not int or type(a) is not float or type(b) is not int or type(b) is not float):    
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
