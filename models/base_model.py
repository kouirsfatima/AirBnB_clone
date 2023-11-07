#!/usr/bin/python3
""" Model for BaseModel class """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Represents the BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        format = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.strptime(value, format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute and save to json """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__

        for key, value in my_dict.items():
            if type(value) is datetime:
                my_dict[key] = value.isoformat()
        return my_dict
