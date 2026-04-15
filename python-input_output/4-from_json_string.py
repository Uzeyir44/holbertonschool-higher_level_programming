#!/usr/bin/python3
"""
This module contains from_json_string function
"""
import json


def from_json_string(my_str):
    """
    This function converts json string
    into python object

    Args:
        my_str: json string
    """
    python_string = json.loads(my_str)
    return(python_string)
