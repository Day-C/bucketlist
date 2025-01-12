#!/usr/bin/python3
"""Handle all user http methods"""

from flask import jsonify, request, abort
from models.user import User
from . import app_view
import models

@app_view.route('/users')
def all_users():
    """retieve all users from storage."""

    #get data from storage
    users = models.file_storage.all(User)
    users_list = []
    for key in users.keys():
        users_list.append(users[key])
    return users_list

@app_view.route('/users/<user_id>')
def one_user(user_id):
    """retive a single user with specific id"""

    user = models.file_storage.get(User, user_id)
    if user != None:
        usr = User(**user)
        return jsonify(usr.to_dict())
    abort(404, "User Not Found")


@app_view.route('/users/<user_id>', methods=["DELETE"])
def remove_user(user_id):
    """delete user"""

    user = models.file_storage.get(User, user_id)
    if user != None:
        print(user)
        inst = User(**user)
        inst.delete()
        return jsonify('{}')
    abort(404, 'User Not Found')

@app_view.route('/users/<user_id>', methods=["PUT"])
def edit_user(user_id):
    """eddit an existing user"""

    user = models.file_storage.get(User, user_id)
    if user != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            for key in data.keys():
                user[key] = data[key]
            inst = User(**user)
            inst.delete()
            upd_user = User(**user)
            upd_user.save()
            return jsonify(upd_user.to_dict())
        abort(400, 'Bad Request')
    abort(404, 'User Not Found')

@app_view.route('/users', methods=['POST'])
def create_user():
    """create a new user"""

    if request.headers['Content-Type'] == 'application/json':
        print(request.headers['Content-Type'])

        data = request.get_json()
        if 'name' not in data:
            abort(400, 'bad Request')
        user = User(**data)
        user.save()
        return jsonify(user.to_dict())
    abort(400, 'Bad Request')
