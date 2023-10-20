import os
import sys
import io
import unittest
from unittest.mock import mock_open, patch

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '..'))

# Method under test
from homework7 import read_file


class TestReadFileFunction(unittest.TestCase):

    @patch('builtins.open', side_effect=FileNotFoundError("File not found"))
    def test_file_not_found(self, mock_open):
        result = read_file("non_existent_file.txt")
        self.assertIsInstance(result, FileNotFoundError)
        self.assertEqual(str(result), "File not found")

    @patch('builtins.open', side_effect=PermissionError("Permission denied"))
    def test_permission_error(self, mock_open):
        result = read_file("some_file.txt")
        self.assertIsInstance(result, PermissionError)
        self.assertEqual(str(result), "Permission denied")

    @patch('builtins.open', side_effect=IOError("IO error"))
    def test_io_error(self, mock_open):
        result = read_file("some_file.txt")
        self.assertIsInstance(result, IOError)
        self.assertEqual(str(result), "IO error")

    @patch('builtins.open', side_effect=Exception("Unexpected error"))
    def test_unexpected_error(self, mock_open):
        result = read_file("some_file.txt")
        self.assertIsInstance(result, Exception)
        self.assertEqual(str(result), "Unexpected error")

    @patch('builtins.open', return_value=io.StringIO("File content"))
    def test_successful_read(self, mock_open):
        result = read_file("some_file.txt")
        self.assertEqual(result, "File content")

if __name__ == '__main__':
    unittest.main()
