#!/usr/bin/python3
"""
This module defines a function to read a text file (UTF8) and print its content to stdout.
"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
