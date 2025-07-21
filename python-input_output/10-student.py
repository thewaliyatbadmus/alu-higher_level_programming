#!/usr/bin/python3
"""This module defines a class Student with attributes and a method
to get a dictionary representation, optionally filtered.
"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are included.
        """
        if (isinstance(attrs, list)
                and all(isinstance(elem, str) for elem in attrs)):
            return {k: getattr(self, k)
                    for k in attrs if hasattr(self, k)}
        return self.__dict__
