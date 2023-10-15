#!/usr/bin/python3
"""
This is the base Model that defines all other classes
It has public and private instances 


"""
from datetime import datetime
import uuid
import models

class BaseModel:
    """
    BaseModel is the base class that defines all common 
    attributes/methods for other classes.

    Attributes:
        id: string - assign with an uuid when an instance is created
        created_at : datetime - assign with the current datetime when 
                     an instance is created
        updated_at: datetime - assign with the current datetime when an instance 
               is created and it will be updated every time you change the object

    """
    def __init__(self, *args, **kwargs):
        """
        Initialises an instance with a dictionary argument

        """
        if kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == "__class__":
                    pass
                else:
                    setattr(self, k, v)

        if "id" not in kwargs:
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs:
            self.created_at = datetime.now()
        if "updated_at" not in kwargs:
            self.updated_at = datetime.now()
        if not kwargs or len(kwargs) == 0:
            models.storage.new(self)

    def __str__(self):
        """ overwrite string special method """
        r = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return r

    def save(self):
        """ update updated_at with current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ return a dict with a key/values of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict
