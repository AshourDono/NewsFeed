# app/repositories/user_repository.py

class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_user(self, user_name: str, email: str, password: str):
        cursor = self.db_connection.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password) 
            VALUES (%s, %s, %s)
        """, (user_name, email, password))
        self.db_connection.commit()
        return cursor.lastrowid

    def get_user(self, user_id: int):
        cursor = self.db_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()

    def update_user(self, user_id: int, user_name: str | None = None, email: str | None = None, password: str | None = None):
        cursor = self.db_connection.cursor()
        update_fields = []
        update_values = []

        if user_name:
            update_fields.append("username = %s")
            update_values.append(user_name)

        if email:
            update_fields.append("email = %s")
            update_values.append(email)

        if password:
            update_fields.append("password = %s")
            update_values.append(password)

        update_values.append(user_id)
        update_query = f"UPDATE users SET {
            ', '.join(update_fields)} WHERE id = %s"

        cursor.execute(update_query, update_values)
        self.db_connection.commit()

    def delete_user(self, user_id: int):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.db_connection.commit()
