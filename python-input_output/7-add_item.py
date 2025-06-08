#!/usr/bin/python3
"""A script that adds all arguments to a file"""


from sys import argv

save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file

if len(argv) > 0:
    my_list = []
    for args in argv:
        my_list.append(args)
    my_list.pop(0)
try:
    old_list = load_from_json("add_item.json")
except FileNotFoundError:
    old_list = []
new_list = old_list + my_list
save_to_json(new_list, "add_item.json")
