#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in objects the obj with key """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file """
        path = FileStorage.__file_path
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

    def reload(self):
        """deserializes the JSON file to objects"""
        try:
            path = FileStorage.__file_path
            with open(path, 'r') as file:
                data = json.load(file)
                for key , value in data.items():
                    if "BaseModel" in key:
                        FileStorage.__objects[key] = BaseModel(**value)
        except:
            pass