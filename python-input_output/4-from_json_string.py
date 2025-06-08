#!/usr/bin/python3
"""Module for converting JSON strings to Python objects"""
import json


def from_json_string(my_str):
    """converts a JSON string to a Python object"""
    return json.loads(my_str)
