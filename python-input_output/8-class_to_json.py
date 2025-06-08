#!/usr/bin/python3
"""Module that define a function to return the dictionary description
for JSON serialization of an object"""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON seialization"""
    return obj.__dict__
