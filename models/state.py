#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import shlex


class State(BaseModel, Base):
    """
    This is the class for State

    Attributes:
    name (str): The name of the state.
    cities (relationship): A relationship to the City class.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        from models import storage
        var = storage.all()
        city_list = []

        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City' and var[key].state_id == self.id):
                city_list.append(var[key])
        return city_list

    def __init__(self, *args, **kwargs):
        """ Initialize State instance """
        super().__init__(*args, **kwargs)
        self.name = ""
