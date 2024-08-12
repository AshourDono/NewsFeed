# app/controllers/post_controller.py

from flask import Response, request, jsonify
from app.services import PostService
from app.exceptions import InvalidDataException, NotFoundException


class PostController:
    def __init__(self, post_service: PostService):
        self.post_service = post_service

    def create_post(self) -> Response:
        try:
            user_id: int = request.json.get('user_id')
            content: str = request.json.get('content')

            # Validate that user_id and content are of the desired types
            if not user_id or not isinstance(user_id, int):
                return jsonify({'error': 'Invalid or missing user_id'}), 400

            if not content or not isinstance(content, str) or len(content) > 300:
                return jsonify({'error': 'Invalid or missing content'}), 400

            # Validate that user_id and content are present
            if not user_id or not content:
                raise InvalidDataException(
                    "User ID and content are required")

            post = self.post_service.create_post(user_id, content)
            return jsonify(post), 201

        except InvalidDataException as e:
            return jsonify({'error': str(e)}), 400

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_post(self, post_id: int) -> Response:
        try:
            post = self.post_service.get_post(post_id)

            if post:
                return jsonify(post)

            raise NotFoundException(f"Post with id {post_id} not found")

        except NotFoundException as e:
            return jsonify({'error': str(e)}), 404

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_post(self, post_id: int) -> Response:
        try:
            content = request.json.get('content')

            # Validate that content is of the desired type
            if not content or not isinstance(content, str) or len(content) > 300:
                return jsonify({'error': 'Invalid or missing content'}), 400

            # Validate that content is present
            if not content:
                raise InvalidDataException(
                    "Content is required to update the post")

            post = self.post_service.update_post(post_id, content)

            if post:
                return jsonify(post)

            raise NotFoundException(f"Post with id {post_id} not found")

        except NotFoundException as e:
            return jsonify({'error': str(e)}), 404

        except InvalidDataException as e:
            return jsonify({'error': str(e)}), 400

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_post(self, post_id: int) -> Response:
        try:
            self.post_service.delete_post(post_id)
            return jsonify({'message': 'Post deleted'}), 204
        except Exception as e:
            return jsonify({'error': str(e)}), 500
