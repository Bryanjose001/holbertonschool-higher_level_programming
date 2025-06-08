#!/usr/bin/python3
"""Module to read and print the contents of a file."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")