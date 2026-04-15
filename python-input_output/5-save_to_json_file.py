#!/usr/bin/python3
"""
This module contains save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function converts given object to json string
    and writes it to the given file

    Args:
        my_obj: python object
        filename: path to the file
    """
    with open(filename, mode="w", encoding="utf-8") as py_obj:
        json_string = json.dumps(my_obj)
        py_obj.write(json_string)
