#!/usr/bin/python3
"""Module for serializing and deserializin data"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes the given data and saves it to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Loads and deserializes data from a pickle file"""
    with open(filename, "r", encoding="utf-8") as file:
        load_data = json.load(file)
    return (load_data)
