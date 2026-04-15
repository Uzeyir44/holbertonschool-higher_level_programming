#!/usr/bin/python3
"""
This module contains class_to_json function
"""
import json


def class_to_json(obj):
    """
    This function converts class instance
    to json string

    Args:
        obj: instances of any class
    """
    json_string = json.dumps(obj)
    return (json_string)
