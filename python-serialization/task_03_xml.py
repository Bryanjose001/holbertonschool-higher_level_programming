#!/usr/bin/python3
"""Method for serialization and deserialization using xml"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize the dictionary into XML and save it to the given filename"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """reads XML data from file and returns deserialized Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
