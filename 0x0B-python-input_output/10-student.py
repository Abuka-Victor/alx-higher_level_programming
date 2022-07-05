#!/usr/bin/python3
""" Module for task 9 """


class Student:
    """ My Student class """
    def __init__(self, first_name, last_name, age):
        """ Initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a serialized version of the object """
        result = dict(self.__dict__)
        if attrs:
            keys = list(result.keys())
            for i in keys:
                if i not in attrs:
                    del result[i]
        return result
