# app/views/post_views.py

from flask import Blueprint
from app.controllers import UserController
from app.services import UserService
from app.repositories import UserRepository
from app.extensions import db_connection

user_views = Blueprint('user_views', __name__)

user_repository = UserRepository(db_connection)
user_service = UserService(user_repository)
user_controller = UserController(user_service)

user_views.url_prefix = '/api'
user_views.route('/users', methods=['POST'])(user_controller.create_user)
user_views.route('/users/<int:user_id>',
                 methods=['GET'])(user_controller.get_user)
user_views.route('/users/<int:user_id>',
                 methods=['PATCH'])(user_controller.update_user)
user_views.route('/users/<int:user_id>',
                 methods=['DELETE'])(user_controller.delete_user)
