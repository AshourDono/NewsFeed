# app/repositories/post_repository.py

class PostRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_post(self, user_id: int, content: str):
        cursor = self.db_connection.cursor()
        cursor.execute("""
            INSERT INTO posts (user_id, content, created_at) 
            VALUES (%s, %s, CURRENT_TIMESTAMP)
        """, (user_id, content))
        self.db_connection.commit()
        return cursor.lastrowid

    def get_post(self, post_id: int):
        cursor = self.db_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
        return cursor.fetchone()

    def update_post(self, post_id: int, content: str):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "UPDATE posts SET content = %s WHERE id = %s", (content, post_id))
        self.db_connection.commit()

    def delete_post(self, post_id: int):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM posts WHERE id = %s", (post_id,))
        self.db_connection.commit()
