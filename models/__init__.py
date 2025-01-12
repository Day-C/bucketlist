#!/usr/bin/python3
"""Connect storage system to interact with models"""

from models.storagengine.file_storage import FileStorage

file_storage = FileStorage()
file_storage.reload()
