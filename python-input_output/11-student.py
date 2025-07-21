#!/usr/bin/python3
"""
Module defines a Student class with JSON serialization
and deserialization capabilities.
"""


class Student:
    """
    Student class with firstname, lastname, and age attributes.

    Methods:
        to_json(attrs=None): returns dict representation filtered by attrs.
        reload_from_json(json): replaces attributes using json dict.
    """

    def __init__(self, firstname, lastname, age):
        """
        Initialize a Student instance.

        Args:
            firstname (str): first name of student
            lastname (str): last name of student
            age (int): age of student
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve dictionary representation of the Student instance.

        Args:
            attrs (list, optional): list of attribute names to include.

        Returns:
            dict: dictionary of requested attributes or all if attrs is None.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from json dict.

        Args:
            json (dict): dictionary with keys as attribute names and values as their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
