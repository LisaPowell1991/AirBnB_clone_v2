#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship(
            "Place", cascade='all, delete, delete-orphan', backref="city")

    def __init__(self, name="", *args, **kwargs):
        """Instantiates a new City"""
        if 'name' not in kwargs:
            self.name = name
        if 'state_id' not in kwargs:
            self.state_id = ""
        super().__init__(*args, **kwargs)
