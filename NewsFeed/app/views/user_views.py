# app/views/user_views.py

from app.blueprints import user_blueprint, user_controller

user_blueprint.route('/users', methods=['POST'])(user_controller.create_user)
user_blueprint.route('/users/<int:user_id>',
                     methods=['GET'])(user_controller.get_user)
user_blueprint.route('/users/<int:user_id>',
                     methods=['PATCH'])(user_controller.update_user)
user_blueprint.route('/users/<int:user_id>',
                     methods=['DELETE'])(user_controller.delete_user)
