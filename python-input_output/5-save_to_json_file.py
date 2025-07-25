#!/usr/bin/python3
"""This module defines a function that writes
an object to a text file as JSON.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
