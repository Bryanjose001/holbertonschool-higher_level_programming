#!/usr/bin/python3
"""Module for loading python objects from JSON files"""
import json


def load_from_json_file(filename):
    """Reads a json file and returns the corresponding python object"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)