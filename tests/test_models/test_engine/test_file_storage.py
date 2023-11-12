#!/usr/bin/python3
""" unittest for test_file_storage """
import unittest
from models.engine.file_storage import FileStorage


class FileStorage_TestCase(unittest.TestCase):

    def test_FileStorage(self):
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertIsInstance(storage._FileStorage__objects, dict)
