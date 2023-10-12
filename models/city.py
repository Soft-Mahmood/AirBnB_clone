#!/usr/bin/python3
"""
this class inherits from Basemodel

"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    This describes the city

    Attributes:
        name: string - empty string.
        state_id : string - empty string: it will be the State.id

    """
    name = ""
    state_id = ""
