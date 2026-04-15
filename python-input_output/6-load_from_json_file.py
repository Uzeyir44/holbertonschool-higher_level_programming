#!/usr/bin/python3
"""
This module contains load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    This function converts json file to
    back to python object

    Args:
        filename: path to the given file
    """
    with open(filename, encoding="utf-8") as json_file:
        json_string = json_file.read()
        return (json.loads(json_string))
