# app/models/user.py

class User:
    def __init__(self, user_name, email, password, id=None):
        self.id = id
        self.user_name = user_name
        self.email = email
        self.password = password
