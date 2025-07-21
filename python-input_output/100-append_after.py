#!/usr/bin/python3
"""
Inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert new_string after each line that contains search_string.

    Args:
        filename (str): name of the file to modify.
        search_string (str): string to search for in each line.
        new_string (str): string to insert after each matching line.
    """
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
