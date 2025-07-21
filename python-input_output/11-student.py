#!/usr/bin/python3
"""Defines a Student class with JSON serialization/deserialization."""


class Student:
    """Student class with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve dictionary representation of Student instance.

        If attrs is a list of strings, only those attributes
        included in attrs are returned.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): dictionary with keys as attribute names
                         and values as attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
