# app/models/like.py

class Like:
    def __init__(self, user_id, post_id, id=None):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
