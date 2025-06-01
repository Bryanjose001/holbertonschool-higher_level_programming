#!/usr/bin/python3
"""check if obj is exactly an instance of a_class"""


def is_same_class(obj, a_class):
    """check if obj is exactly an instance of a_class"""
    return type(obj) is a_class
