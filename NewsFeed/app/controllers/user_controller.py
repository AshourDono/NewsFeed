# app/controllers/user_controller.py

from flask import Response, request, jsonify
from marshmallow import ValidationError
from mysql.connector import Error as MySQLError
from app.services import UserService
from app.exceptions import NotFoundException
from app.schemas import user_create_schema, user_update_schema


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self) -> Response:
        try:
            # Load and validate the input data using the schema
            user_data = user_create_schema.load(request.json)

            user_name: str = user_data['user_name']
            email: str = user_data['email']
            password: str = user_data['password']

            # Proceed with user creation
            user = self.user_service.create_user(user_name, email, password)
            return jsonify(user), 201

        except ValidationError as e:
            # Handle schema validation errors
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
            # Load and validate the input data
            user_data = user_update_schema.load(request.json)

            user_name: str | None = user_data.get('user_name')
            email: str | None = user_data.get('email')
            password: str | None = user_data.get('password')

            # Perform the update
            user = self.user_service.update_user(
                user_id, user_name, email, password
            )

            if user:
                # Assuming 200 OK for successful update
                return jsonify(user), 200

            raise NotFoundException(f"User with ID {user_id} not found")

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
            return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

    def delete_user(self, user_id: int) -> Response:
        try:
            self.user_service.delete_user(user_id)
            return jsonify({'message': 'user deleted'}), 204
        except Exception as e:
            return jsonify({'error': str(e)}), 500
