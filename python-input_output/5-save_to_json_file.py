#!/usr/bin/python3
"""
This module contains save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, encoding="utf-8") as py_obj:
        json_string = json.dumps(my_obj)
        py_obj.write(json_string)
