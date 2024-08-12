# app/views/post_views.py

from app.blueprints import post_blueprint, post_controller

post_blueprint.route('/posts', methods=['POST'])(post_controller.create_post)
post_blueprint.route('/posts/<int:post_id>',
                     methods=['GET'])(post_controller.get_post)
post_blueprint.route('/posts/<int:post_id>',
                     methods=['PATCH'])(post_controller.update_post)
post_blueprint.route('/posts/<int:post_id>',
                     methods=['DELETE'])(post_controller.delete_post)
