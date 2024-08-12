# app/models/follow.py

class Follow:
    def __init__(self, follower_id: int, followee_id: int, id: int | None = None):
        self.id = id
        self.follower_id = follower_id
        self.followee_id = followee_id
