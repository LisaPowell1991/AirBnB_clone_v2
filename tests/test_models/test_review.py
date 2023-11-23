#!/usr/bin/python3
""" Test module for Review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ TestReview class to test the functionality of Review class """

    def __init__(self, *args, **kwargs):
        """ Initialization method """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test the type of place_id attribute """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test the type of user_id attribute """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test the type of text attribute """
        new = self.value()
        self.assertEqual(type(new.text), str)
