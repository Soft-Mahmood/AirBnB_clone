#!/usr/bin/python3
"""
this class inherits from Basemodel

"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    This describes reviews

    Attributes:
        place_id : string - empty string
        user_id : string - empty string
        text : string - empty string

    """
    place_id = ""
    user_id = ""
    text = ""
