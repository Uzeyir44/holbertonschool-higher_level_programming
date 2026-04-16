#!/usr/bin/python3
"""
This module contains serialize_and_save_to_file
and load_and_deserialize functions
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    This function serializes data and owerwrites given file
    with serialized data

    Args:
        data: data structure to be serialized
        filename: path to the file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(data))

def load_and_deserialize(filename):
    """
    This function deserializes file and and returns data

    Args:
        filename: path to the file

    Return:
        deserialized json file
    """
    with open(filename, encoding="utf-8") as file:
        return(json.loads(file))
