#!/usr/bin/python3
"""testing project models"""

from models.base_model import Base_mod
from models.user import User
from models.post import Post
from models.comment import Comment
import models


inst = Base_mod()
#print(inst)
inst.delete()
user = User()
#print(user)
user.save()
data = user.to_dict()
print(data)
#user.delete()
rev = Comment()
#print(rev)
rev.save()
#rev.delete()

post = Post()
post.save()
#print(post)
print(models.file_storage.get(Post, '9287c7fb-eb96-4d2b-9bdf-722f8b684066'))

print(models.file_storage.count(Post))
ins = models.file_storage.all(Post)
print(ins)
"""
dom = User(**data)
dom.delete()"""
print(data)
data = {'updated_at': '2024-09-29T15:21:03:876188', 'created_at': datetime.datetime(2024, 9, 29, 15, 21, 3, 876160), 'id': '2bad29d8-9f02-4ce5-b6a1-5057db2c7591'}

inst = User(**data)
print(inst)
#print(models.file_storage.get(User, '5637150a-1a21-45c0-8f65-64d5b7bd8d35'))
