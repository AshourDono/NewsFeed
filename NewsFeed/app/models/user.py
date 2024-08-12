# app/models/user.py

class User:
    def __init__(self, user_name: str, email: str, password: str, id: int | None = None):
        self.id = id
        self.user_name = user_name
        self.email = email
        self.password = password
