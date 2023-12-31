#!/usr/bin/python3
""" unittest for BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class BaseModelTestCase(unittest.TestCase):
    """class for basemodel tests"""

    def test_BaseModel(self):
        """attributes existance"""
        new = BaseModel()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        """Methodes existance"""
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """type test"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)

    def test_str(self):
        """test correct output for str method"""
        new = BaseModel()
        output = f"[{new.__class__.__name__}] ({new.id}) {new.__dict__}"
        self.assertEqual(str(new), output)

    def test_save(self):
        """test for save method"""
        obj = BaseModel()
        old_date = obj.updated_at
        obj.save()
        self.assertGreater(old_date, obj.created_at)
        with patch('models.storage.save') as mock:
            new = BaseModel()
            new.save()
            mock.assert_called_once()

    def test_to_dict(self):
        """test count key"""
        Td = BaseModel()
        key = Td.to_dict().keys()
        self.assertCountEqual(
            key, ['id', 'created_at', 'updated_at', '__class__'])
