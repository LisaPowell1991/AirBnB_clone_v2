#!/usr/bin/python3

"""Unittest module for testing the Amenity class"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test case for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes a test instance of Amenity"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test the 'name' attribute of the Amenity class """
        new = self.value()
        self.assertEqual(type(new.name), str)
