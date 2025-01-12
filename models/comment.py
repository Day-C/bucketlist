#!/usr/bin/python3
"""create review attributes"""

from models.base_model import Base_mod


class Comment(Base_mod):
    """define review instance attributes"""

    user_id = ""
    post_id = ""
    test = ""
