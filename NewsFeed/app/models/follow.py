# app/models/follow.py

class Follow:
    def __init__(self, id, follower_id, followee_id):
        self.id = id
        self.follower_id = follower_id
        self.followee_id = followee_id
