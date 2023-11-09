#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel."""
    
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

