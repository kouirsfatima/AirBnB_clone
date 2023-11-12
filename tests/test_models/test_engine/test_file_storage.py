#!/usr/bin/python3
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import os


class Test_FileStorage(unittest.TestCase):
    """This Class for test FileStorage"""

    def test_hasattr_and_type(self):
        """test has attribute"""
        obj = FileStorage()

        """test has privet class attribute"""
        self.assertTrue(hasattr(obj, "_FileStorage__file_path"))
        self.assertTrue(hasattr(obj, "_FileStorage__objects"))

        """test"""
        _file = models.storage._FileStorage__file_path
        _obj = models.storage._FileStorage__objects
        self.assertEqual(_file, "file.json")
        self.assertEqual(type(_file), str)
        self.assertEqual(type(_obj), dict)

    def test_all_models(self):
        """Test all method"""
        my_obj = BaseModel()

        """test all"""
        self.assertEqual(type(models.storage.all()), dict)
        self.assertNotEqual(models.storage.all(), {})
        """existence id"""
        self.assertTrue(hasattr(my_obj, "id"))
        self.assertEqual(type(my_obj.id), str)

        """Test: my_obj"""
        Cls_id = f"BaseModel.{my_obj.id}"
        self.assertIsInstance(models.storage.all()[Cls_id], BaseModel)
        self.assertEqual(models.storage.all()[Cls_id], my_obj)
        """ Test: check if object exist by Cls_id """
        self.assertIn(Cls_id, models.storage.all())
        """ Test: check if the object found in storage with corrrect id"""
        self.assertTrue(models.storage.all()[Cls_id] is my_obj)

        """Test: save"""
        models.storage.save()
        with open("file.json", 'r') as file:
            saved_data = json.load(file)
        """ Test: check if object exist by Cls_id """
        self.assertIn(Cls_id, saved_data)
        """ Test: check if the value found in json is correct"""
        self.assertEqual(saved_data[Cls_id], my_obj.to_dict())

        """Test: reload"""
        models.storage.all().clear()
        models.storage.reload()
        with open("file.json", 'r') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data[Cls_id],
                         models.storage.all()[Cls_id].to_dict())


if __name__ == '__main__':
    unittest.main()
