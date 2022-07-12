#!/usr/bin/python3
""" My base class module """


class Base:
    """ My Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization method """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
