# app/services/post_service.py

from app.repositories import PostRepository


class PostService:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def create_post(self, user_id: int, content: str):
        post_id = self.post_repository.create_post(user_id, content)
        return self.post_repository.get_post(post_id)

    def get_post(self, post_id: int):
        return self.post_repository.get_post(post_id)

    def update_post(self, post_id: int, content: str):
        self.post_repository.update_post(post_id, content)
        return self.post_repository.get_post(post_id)

    def delete_post(self, post_id: int):
        self.post_repository.delete_post(post_id)
