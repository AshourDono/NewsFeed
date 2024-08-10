# app/services/post_service.py

from app.models import User
from app.repositories import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_name, email, password):
        post_id = self.user_repository.create_user(user_name, email, password)
        return self.user_repository.get_user(post_id)

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)

    def update_user(self, user_id, user_name, email, password):
        self.user_repository.update_user(user_id, user_name, email, password)
        return self.user_repository.get_user(user_id)

    def delete_user(self, user_id):
        self.user_repository.delete_user(user_id)
