#!/usr/bin/python3
"""Module define student class"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the student instance"""
        result = {}
        if attrs is None:
            return self.__dict__
        result = {}
        for key in attrs:
            if key in self.__dict__:
                result[key] = self.__dict__[key]

        return result

    def reload_from_json(self, json):
        """Update the instance attribute from a given dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
