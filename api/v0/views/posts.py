#!/usr/bin/python3
"""Posts http method handlers"""

from flask import jsonify, request, abort
from models.post import Post
from . import app_view
import models

@app_view.route('/posts')
def all_post():
    """get all post"""

    posts = models.file_storage.all(Post)
    if posts != None:
        all_posts = []
        for key in posts.keys():
            all_posts.append(posts[key])
        return jsonify(all_posts)
    abort(404)

@app_view.route('/posts/<post_id>')
def one_post(post_id):
    """get one posts"""

    post = models.file_storae.get(Post, post_id)
    if post != None:
        return jsonify(post)
    abort(404)

@app_view.route('/posts/<post_id>', methods=["DELETE"])
def delete_post(post_id):
    """delete an existring post"""

    post = models.file_storage.get(Post, post_id)
    if post != None:
        # check ifuser is the author
        '''if post['user_id'] == usrid:
            Delete the post'''

        inst = Post(**post)
        inst.delete()
        return jsonify('{}')
    abort(404)

@app_view.route('/posts/<post_id>', methods=['PUT'])
def edit_post(post_id):
    """make chanes to a post"""

    post = models.file_storage.get(Post, post_id)
    if post != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            #delete post
            inst = Post(**post)
            inst.delete()
            #create new post
            for key in data.keys():
                post[key] = data[key]
            new_post = Post(**post)
            new_post.save()
            return jsonify(new_post.to_dict())
        abort(400)
    abort(404)

@app_view.route('/posts', methods=['POST'])
def create_post():
    """create a new post"""

    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        #create new post
        post = Post(**data)
        post.save()
        return jsonify(post.to_dict())
    abort(400)
