#!/usr/bin/python3
"""
this class inherits from Basemodel

"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    This describes a user that joins the platform

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""    
