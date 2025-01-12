#!/usr/bin/python3
"""define user attributes"""

from models.base_model import Base_mod

class User(Base_mod):
    """Define a user instance"""

    name = ""
    email = ""
    password = ""
    prodfession = ""
