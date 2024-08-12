# app/controllers/post_controller.py

from flask import Response, request, jsonify
from marshmallow import ValidationError
from mysql.connector import Error as MySQLError
from app.services import PostService
from app.exceptions import NotFoundException
from app.schemas import post_create_schema, post_update_schema


class PostController:
    def __init__(self, post_service: PostService):
        self.post_service = post_service

    def create_post(self) -> Response:
        try:
            post_data = post_create_schema.load(request.json)

            user_id: int = post_data['user_id']
            content: str = post_data['content']

            post = self.post_service.create_post(user_id, content)
            return jsonify(post), 201

        except ValidationError as e:
            return jsonify(e.messages), 400

        except MySQLError as e:
            # Handle specific MySQL error codes
            if e.errno == 1062:
                return jsonify({'error': 'Duplicate entry (unique constraint violation).'}), 400
            elif e.errno in {1451, 1452}:
                return jsonify({'error': 'Foreign key constraint violation.'}), 400
            else:
                return jsonify({'error': f"Database error occurred: {str(e)}"}), 500

        except Exception as e:
            # Handle unexpected errors
            return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

    def get_post(self, post_id: int) -> Response:
        try:
            post = self.post_service.get_post(post_id)

            if post:
                return jsonify(post)

            raise NotFoundException(f"Post with id {post_id} not found")

        except NotFoundException as e:
            return jsonify({'error': str(e)}), 404

        except MySQLError as e:
            # Handle specific MySQL error codes
            if e.errno == 1062:
                return jsonify({'error': 'Duplicate entry (unique constraint violation).'}), 400
            elif e.errno in {1451, 1452}:
                return jsonify({'error': 'Foreign key constraint violation.'}), 400
            else:
                return jsonify({'error': f"Database error occurred: {str(e)}"}), 500

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_post(self, post_id: int) -> Response:
        try:
            post_data = post_update_schema.load(request.json)

            content: str = post_data['content']

            post = self.post_service.update_post(post_id, content)

            if post:
                return jsonify(post)

        except ValidationError as err:
            return jsonify(err.messages), 400

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_post(self, post_id: int) -> Response:
        try:
            self.post_service.delete_post(post_id)
            return jsonify({'message': 'Post deleted'}), 204
        except Exception as e:
            return jsonify({'error': str(e)}), 500
