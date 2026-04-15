#!/usr/bin/python3
import json
"""
This module contains to_json_string function
"""


def to_json_string(my_obj):
    """
    This function converts python object
    into json string

    Args:
        my_obj: python object
    """
    json_string = json.dumps(my_obj)
