#!/usr/bin/python3
"""Check if an object inherits from a class (not direct instance)"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass"""
    return isinstance(obj, a_class) and type(obj) is not a_class
