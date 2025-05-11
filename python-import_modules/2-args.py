#!/usr/bin/python3
"""A script that prints the number of arguments and lists them."""

import sys

if __name__ == "__main__":
    # Get command-line arguments excluding the script name
    args = sys.argv[1:]

    # Count the number of arguments
    num_args = len(args)

    # If no arguments were passed, print a special message
    if num_args == 0:
        print("0 arguments.")
    else:
        # Print number of arguments with correct grammar
        print(f"{num_args} argument{'s' if num_args != 1 else ''}:")
        # Print each argument with its index
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")