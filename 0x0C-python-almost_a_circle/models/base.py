#!/usr/bin/python3
""" Module that contains class Base """
import json
import os
import csv


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
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
        """ JSON string to dictionary """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)
        lst = []
        if os.path.isfile(filename) is False:
            pass
        else:
            with open(filename, 'r') as file:
                data = file.read()

            list_output = cls.from_json_string(data)

            for dic in list_output:
                new = cls.create(**dic)
                lst.append(new)

        return lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = "{}.csv".format(cls.__name__)
        lst = []
        if cls.__name__ == "Rectangle":
            fieldnames = ['x', 'y', 'id', 'height', 'width']
        else:
            fieldnames = ['x', 'y', 'id', 'size']

        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                dic = obj.to_dictionary()
                lst.append(dic)
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in lst:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)
        lst = []

        if os.path.isfile(filename) is False:
            pass
        else:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for dic in reader:
                    for k, v in dic.items():
                        dic[k] = int(v)
                    new = cls.create(**dic)
                    lst.append(new)

        return lst
