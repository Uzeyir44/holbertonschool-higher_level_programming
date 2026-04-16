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
    with open(filename, mode="w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    This function deserializes file and and returns data

    Args:
        filename: path to the file

    Return:
        deserialized json file
    """
    with open(filename, mode='rb') as file:
        return(json.load(file))

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)