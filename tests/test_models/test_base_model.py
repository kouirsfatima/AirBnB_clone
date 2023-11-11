#!/usr/bin/python3
""" unittest for BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch

class BaseModelTestCase(unittest.TestCase):
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
        with patch('models.storage.save') as mock_function:
            obj.save()
            mock_function.assert_called_once()
        
