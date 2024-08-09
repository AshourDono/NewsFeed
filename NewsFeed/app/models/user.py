# app/models/user.py

class User:
    def __init__(self, id, user_name, email, password):
        self.id = id
        self.user_name = user_name
        self.email = email
        self.password = password
