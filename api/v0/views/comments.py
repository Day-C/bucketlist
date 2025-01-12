#!/usr/bin/python3
"""Review http methods handler"""

from flask import jsonify, request, abort
from models.comment import Comment
from models.post import Post
from . import app_view
import models

@app_view.route('/posts/<post_id>/comments')
def posts_comments(post_id):
    """retrive all comment under a post"""

    #find post
    post = models.file_storage.get(Post, post_id)
    if post != None:
        #retrieve all comments
        comments = models.file_storage.all(Comment)
        comment_list = []
        for key in comments.keys():
            if comment[key]['post_id'] == post_id:
                comment_list.append(comment[key])
        return jsonify(comment_list)

@app_view.route('/comments/<comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    """Delete specified comment"""

    #get all comments
    comment = models.file_storage.get(Comment, comment_id)
    if comment != None:
        comments = models.file_storage.all(Comment)
        for key in comments.keys():
            if comments[key]['id'] == comment_id:
                inst = Comment(**comments[key])
                inst.delete()
        return jsonify('{}')
    abort(404, 'Comment Not Found')


@app_view.route('/comments/<comment_id>', methods=['PUT'])
def edit_comment(comment_id):
    """edit an existing user"""

    comment = models.file_storage.get(Comment, comment_id)
    if comment != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            if 'text' in data:
                comment[text] = data['text']
            inst = Comment(**comment)
            inst.delete()
            comm = Comment(**comment)
            comm.save()
            return jsonify(comm.to_dict())
        abort(404, 'Bad Request')
    abort(404)


@app_view.route('/post/<post_id>/comment', methods=['POST'])
def create_comment(post_id):
    """Create a new comment for a post"""

    post = models.file_storage.get(Post, post_id)
    if post != None:
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            data['post_id'] = post_id
            comment = Comment(**data)
            return jsonify(comment)
        abort(400)
    abort(404)
