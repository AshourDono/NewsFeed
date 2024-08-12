# app/controllers/user_controller.py

from flask import Response, request, jsonify
from app.services import UserService
from app.exceptions import InvalidDataException, NotFoundException


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self) -> Response:
        try:
            user_name: str = request.json.get('user_name')
            email: str = request.json.get('email')
            password: str = request.json.get('password')

            # Validate provided fields
            if not user_name or not isinstance(user_name, str) or len(user_name) < 3 or len(user_name) > 30:
                return jsonify({'error': 'Invalid or missing user_name'}), 400

            if not email or not isinstance(email, str):
                return jsonify({'error': 'Invalid or missing email'}), 400

            if not password or not isinstance(password, str) or len(password) < 8 or len(password) > 50:
                return jsonify({'error': 'Invalid or missing password'}), 400

            # Check if all of the fields are provided
            if not user_name or not email or not password:
                raise InvalidDataException(
                    "Username, email and password are required")

            user = self.user_service.create_user(user_name, email, password)
            return jsonify(user), 201

        except InvalidDataException as e:
            return jsonify({'error': str(e)}), 400

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_user(self, user_id: int) -> Response:
        try:
            user = self.user_service.get_user(user_id)

            if user:
                return jsonify(user)

            raise NotFoundException(f"user with id {user_id} not found")

        except NotFoundException as e:
            return jsonify({'error': str(e)}), 404

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_user(self, user_id: int) -> Response:
        try:
            # Get the values from the request
            user_name = request.json.get('user_name')
            email = request.json.get('email')
            password = request.json.get('password')

            # Check if any of the fields are provided
            if not user_name and not email and not password:
                raise InvalidDataException(
                    "At least one of 'user_name', 'email', or 'password' must be provided"
                )

            # Validate provided fields
            if user_name is not None and (not isinstance(user_name, str) or len(user_name) < 3 or len(user_name) > 30):
                return jsonify({'error': 'Invalid user_name'}), 400

            if email is not None and (not isinstance(email, str) or len(email) > 50):
                return jsonify({'error': 'Invalid email'}), 400

            if password is not None and (not isinstance(password, str) or len(password) < 8 or len(password) > 50):
                return jsonify({'error': 'Invalid password'}), 400

            # Perform the update
            user = self.user_service.update_user(
                user_id, user_name, email, password
            )

            if user:
                return jsonify(user)

            raise NotFoundException(f"user with id {user_id} not found")

        except NotFoundException as e:
            return jsonify({'error': str(e)}), 404

        except InvalidDataException as e:
            return jsonify({'error': str(e)}), 400

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_user(self, user_id: int) -> Response:
        try:
            self.user_service.delete_user(user_id)
            return jsonify({'message': 'user deleted'}), 204
        except Exception as e:
            return jsonify({'error': str(e)}), 500
