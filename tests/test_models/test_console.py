import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel
from console import HBNBCommand

 def test_create_with_valid_parameters(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel name="example" age=25')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Length of the UUID

    def test_create_with_invalid_class_name(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create InvalidClass name="example"')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_create_with_missing_class_name(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_with_invalid_parameter(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel invalid_param="value"')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** invalid parameter: invalid_param=value **")

    def test_create_with_quoted_string_value(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel name="My_house"')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Length of the UUID

    def test_create_with_float_value(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel value=3.14')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Length of the UUID

    def test_create_with_integer_value(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel number=42')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Length of the UUID

    def test_create_with_updated_at_parameter(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel updated_at="2022-01-01T00:00:00"')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Length of the UUID

    def test_create_without_updated_at_parameter(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd('create BaseModel name="example"')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Length of the UUID

            # Verify that the created instance has a valid 'updated_at' attribute
            created_instance_id = output
            created_instance = BaseModel(id=created_instance_id)
            self.assertTrue(isinstance(created_instance.updated_at, datetime))


if __name__ == '__main__':
    unittest.main()