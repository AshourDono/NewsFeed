# app/controllers/post_controller.py

from flask import request, jsonify
from app.services import PostService


class PostController:
    def __init__(self, post_service: PostService):
        self.post_service = post_service

    def create_post(self):
        user_id = request.json.get('user_id')
        content = request.json.get('content')
        post = self.post_service.create_post(user_id, content)
        return jsonify(post), 201

    def get_post(self, post_id):
        post = self.post_service.get_post(post_id)
        if post:
            return jsonify(post)
        return jsonify({'message': 'Post not found'}), 404

    def update_post(self, post_id):
        content = request.json.get('content')
        post = self.post_service.update_post(post_id, content)
        return jsonify(post)

    def delete_post(self, post_id):
        self.post_service.delete_post(post_id)
        return jsonify({'message': 'Post deleted'}), 204
