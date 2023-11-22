import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Set up any resources needed for the tests. """
        pass

    @classmethod
    def tearDownClass(cls):
        """ Clean up any resources used for the tests. """
        pass

    def setUp(self):
        """ Set up any resources specific to an individual test. """
        self.hbnb_command = HBNBCommand()

    def tearDown(self):
        """ Clean up any resources used in the test. """
        pass

    def test_do_quit(self):
        """ Test the do_quit method. """
        with self.assertRaises(SystemExit):
            self.hbnb_command.do_quit(None)

    
if __name__ == '__main__':
    unittest.main()
