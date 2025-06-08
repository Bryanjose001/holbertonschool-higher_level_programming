#!/usr/bin/python3
"""module for converting Python obj to json strings"""
import json


def to_json_string(my_obj):
    """converts a Python obj to a json string"""
    return json.dumps(my_obj)
