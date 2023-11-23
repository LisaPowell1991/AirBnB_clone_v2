#!/usr/bin/python3
""" This module contains unit tests for the Place class. """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test cases for the Place class. """

    def __init__(self, *args, **kwargs):
        """ Initializes a test instance of the Place class. """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test the data type of the city_id attribute. """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test the data type of the user_id attribute. """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test the data type of the name attribute. """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test the data type of the description attribute. """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test the data type of the number_rooms attribute. """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test the data type of the number_bathrooms attribute. """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test the data type of the max_guest attribute. """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test the data type of the price_by_night attribute. """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test the default value of the latitude attribute. """
        new = Place()
        self.assertIsNone(new.latitude)

    def test_longitude(self):
        """ Test the default value of the longitude attribute. """
        new = Place()
        self.assertIsNone(new.latitude)

    def test_amenity_ids(self):
        """ Test the data type of the amenity_ids attribute. """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
