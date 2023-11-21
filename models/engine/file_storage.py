#!/usr/bin/python3

"""This is the file storage class for AirBnB"""

import json

from models.base_model import BaseModel

from models.user import User

from models.state import State

from models.city import City

from models.amenity import Amenity

from models.place import Place

from models.review import Review

import shlex


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary or a list of objects in the internal storage,
        filtered by class type if provided.
        Args:
            cls (Optional): The class type for filtering objects.
            If cls is None, return all objects.
        Returns:
            Dict or List: A dictionary or a list of objects.
        """
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_dict = {
                    key: value for key, value in FileStorage.__objects.items()
                    if isinstance(value, cls)
                    }
            return filtered_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        key = obj.to_dict()['__class__'] + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serialize the file path to JSON file path
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp =
            {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """
        serialize the file path to JSON file path
        """
        from models.base_model import BaseModel
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
                    class_name = val['__class__']
                    if class_name in classes:
                        self.all()[key] = classes[class_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete an existing element
        """
        if obj is not None:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            self.all().pop(key, None)

    def close(self):
        """calls reload()
        """
        self.reload()
