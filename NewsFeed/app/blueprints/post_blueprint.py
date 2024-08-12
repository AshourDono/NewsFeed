# app/blueprints/post_blueprint

from flask import Blueprint
from app.controllers import PostController
from app.services import PostService
from app.repositories import PostRepository
from app.extensions import db_connection

post_blueprint = Blueprint('post_blueprint', __name__, url_prefix='/api')

post_repository = PostRepository(db_connection)
post_service = PostService(post_repository)
post_controller = PostController(post_service)
