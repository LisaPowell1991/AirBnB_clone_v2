#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary or a filtered dictionary
        of models currently in storage
        """
        from models import storage
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_dict = {}
            for key, value in FileStorage.__objects.items():
                if key.split('.')[0] == cls.__name__:
                    filtered_dict[key] = value
            return filtered_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        from models import storage
        key = obj.to_dict()['__class__'] + '.' + obj.id
        self.all()[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        from models import storage
        with open(storage.__file_path, 'w') as f:
            temp = {
                    key: val.to_dict() for key,
                    val in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models import storage
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        from models import storage
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            self.all().pop(key, None)

    def close(self):
        """
        Closes the storage by calling the reload() method
        for deserializing the JSON file to objects.
        """
        self.reload()
