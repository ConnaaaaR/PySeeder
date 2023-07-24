import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from commandline import generator, Person, Address, User, connect_to_database, exporter


class TestExporter(unittest.TestCase):
    test_data = {
            'class_name': 'Person',
            'instances': [{'fname': 'John', 'lname': 'Doe'}, {'fname': 'Jane', 'lname': 'Smith'}]}

    @patch('builtins.input', side_effect=['csv'])
    @patch('commandline.generator', return_value=test_data)
    def test_exporter_csv(self, mock_generator, mock_input):
        result = exporter()
        self.assertEqual(result, 'done!')

    @patch('builtins.input', side_effect=['json'])
    @patch('commandline.generator', return_value=test_data)
    def test_exporter_json(self, mock_generator, mock_input):
        result = exporter()
        self.assertEqual(result, 'done!')

    @patch('builtins.input', side_effect=['invalid_format', 'json'])  # Test invalid format, then valid format
    @patch('commandline.generator', return_value=test_data)
    def test_exporter_invalid_format_then_valid(self, mock_generator, mock_input):
        result = exporter()
        self.assertEqual(result, 'error')


if __name__ == '__main__':
    unittest.main()
