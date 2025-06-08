#!/usr/bin/python3
"""Module for writing text to a file"""


def write_file(filename="", text=""):
    """writes the given text to utf-8 text file"""

    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))
