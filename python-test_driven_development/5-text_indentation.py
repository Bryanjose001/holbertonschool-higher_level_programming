#!/usr/bin/python3
"""
Module Name: 5-text_indentation.py
Description: prints a text with 2 new lines after each'., ? and :'
Authors: Lusanco, Ltoro9, Antoniofdjs Date: Feb 01 2024
"""


def text_indentation(text):
    """Description: prints a text with 2 new lines after each'., ? and :'
    - text: is a string
    - c: is int"""
    err = "text_indentation() missing 1 required positional argument: 'text'"
    if text is None:
        raise TypeError(err)
    if type(text) is not str:
        raise TypeError("text must be a string")
    if not text:
        raise TypeError("Text is empty")
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            while c + 1 < len(text) and text[c + 1] == " ":
                c += 1
        c += 1
