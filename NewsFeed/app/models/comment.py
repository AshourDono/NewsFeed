# app/models/comment.py

class Comment:
    def __init__(self, user_id: int, post_id: int, content: str, created_at: str, id: int | None = None):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
        self.content = content
        self.created_at = created_at
