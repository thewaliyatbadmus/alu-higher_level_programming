#!/usr/bin/python3
"""
Defines the Student class for serialization and deserialization.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student.

        If attrs is a list of strings, only the named attributes
        are retrieved. Otherwise, all attributes are returned.

        Args:
            attrs (list, optional): List of attribute names.

        Returns:
            dict: Dictionary of attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary with keys as attribute names
                         and values as the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
