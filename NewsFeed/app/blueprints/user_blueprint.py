# app/blueprints/user_blueprint

from flask import Blueprint
from app.controllers import UserController
from app.services import UserService
from app.repositories import UserRepository
from app.extensions import db_connection

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/api')

user_repository = UserRepository(db_connection)
user_service = UserService(user_repository)
user_controller = UserController(user_service)
