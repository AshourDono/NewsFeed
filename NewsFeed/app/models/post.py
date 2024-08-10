# app/models/post.py

class Post:
    def __init__(self, user_id, content, created_at, id=None):
        self.id = id
        self.user_id = user_id
        self.content = content
        self.created_at = created_at
