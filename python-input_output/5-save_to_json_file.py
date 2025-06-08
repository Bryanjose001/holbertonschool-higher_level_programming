#!/usr/bin/python3
"""module for saving Python objects to json files"""
import json


def save_to_json_file(my_obj, filename):
    """write a python object to a text file using json format"""
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
