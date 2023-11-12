#!/usr/bin/python3
""" unittest for test_file_storage """
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
    
    def test_FileStorage(self):
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))
