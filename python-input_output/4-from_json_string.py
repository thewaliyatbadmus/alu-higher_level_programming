#!/usr/bin/python3
"""This module defines a function that returns
an object by decoding a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string.
    """
    return json.loads(my_str)
