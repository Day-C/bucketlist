#!/usr/bin/python3
"""create blueprint"""

from flask import Blueprint

app_view = Blueprint('app_view', __name__, url_prefix='/api/v0')

from .users import *
from .comments import *
from .posts import *

