#!/usr/bin/python3
"""
This class serialises instances to a JSON file
and also deserialises JSON files to instances.

"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    Handles the serialisation and deserialisation 

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets obj with fresh id value """
        fresh_id = "{}.{}".format(type(obj).__name__, str(obj.id))
        self.__objects[fresh_id] = obj

    def save(self):
        """ serializes object """
        with open(self.__file_path, 'w') as myFile:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()},
                      myFile)

    def reload(self):
        """ deserializes a json file """
        try:
            with open('file.json') as myFile:
                f = json.load(myFile)
            for k, v in f.items():
                if "BaseModel" in k:
                    self.__objects[k] = BaseModel(**v)
                elif "User" in k:
                    self.__objects[k] = User(**v)
                elif "Place" in k:
                    self.__objects[k] = Place(**v)
                elif "State" in k:
                    self.__objects[k] = State(**v)
                elif "City" in k:
                    self.__objects[k] = City(**v)
                elif "Amenity" in k:
                    self.__objects[k] = Amenity(**v)
                elif "Review" in k:
                    self.__objects[k] = Review(**v)
        except:
            pass
