#!/usr/bin/python3
"""post object attribures"""

from models.base_model import Base_mod


class Post(Base_mod):
    """define a posts attributes."""

    user_id = ""
    text: ""
    comments = ""
