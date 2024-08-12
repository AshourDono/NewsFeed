# app/models/share.py

class Share:
    def __init__(self, user_id: int, post_id: int, id: int | None = None):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
