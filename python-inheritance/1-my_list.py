#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """A list subclass with a method to print a sorted list"""
    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
