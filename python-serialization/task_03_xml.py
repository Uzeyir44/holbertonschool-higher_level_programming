#!/usr/bin/python3
"""
This module contains serialize_to_xml and
deserialize_from_xml functions
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    This functoin serializes dictionary object
    into xml document

    Args:
        dictionary (dict): python object
        filename: path to the xml document
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = value
    tree = ET.ElementTree(root)
    tree.write(
            filename,
            encoding='utf-8',
            xml_declaration=True
            )


def deserialize_from_xml(filename):
    """
    This function deserializes xml document
    into python dictionary

    Args:
        filename: path to the xml document

    Returns:
        (dict): deserialized xml document
    """
    tree = ET.parse(filename)
    dictionary = {}
    root = tree.getroot()
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
