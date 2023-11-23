#!/usr/bin/python3
""" Module for testing the City class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Test class for the City model """

    def __init__(self, *args, **kwargs):
        """ Initializes a test instance of the City class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test the state_id attribute of the City class """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Test the name attribute of the City class """
        new = self.value()
        self.assertEqual(type(new.name), str)
