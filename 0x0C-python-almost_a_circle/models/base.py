#!/usr/bin/python3

import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        filename = "{}.json".format(cls.__name__)
        lst = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                lst.append(dictionary)
            json_dictionary = cls.to_json_string(lst)
            with open(filename, "w") as f:
                f.write(json_dictionary)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        instance = cls(1, 1)
        instance.update(**dictionary)
        return instance
