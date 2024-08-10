from faker import Faker
from app.extensions import db_connection

fake = Faker()


def create_fake_newsfeed_data(users=10, posts=5, likes=1, shares=1, comments=1):
    cursor = db_connection.cursor()

    for _ in range(users):
        user_name = fake.user_name()
        email = fake.email(safe=True)
        password = fake.password(
            length=36, special_chars=True, digits=True, upper_case=True, lower_case=True)

        # Insert user into the database
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (user_name, email, password)
        )
        db_connection.commit()

        user_id = cursor.lastrowid  # Get the ID of the last inserted user

        for _ in range(posts):
            content = fake.text(max_nb_chars=300)
            created_at = fake.date_time_this_year()

            # Insert post into the database
            cursor.execute(
                "INSERT INTO posts (user_id, content, created_at) VALUES (%s, %s, %s)",
                (user_id, content, created_at)
            )
            db_connection.commit()

            post_id = cursor.lastrowid  # Get the ID of the last inserted post

            for _ in range(likes):
                # Insert like into the database
                cursor.execute(
                    "INSERT INTO likes (user_id, post_id) VALUES (%s, %s)",
                    (user_id, post_id)
                )
                db_connection.commit()

            for _ in range(shares):
                # Insert share into the database
                cursor.execute(
                    "INSERT INTO shares (user_id, post_id) VALUES (%s, %s)",
                    (user_id, post_id)
                )
                db_connection.commit()

            for _ in range(comments):
                comment_content = fake.text(max_nb_chars=300)
                comment_created_at = fake.date_time_this_year()

                # Insert comment into the database
                cursor.execute(
                    "INSERT INTO comments (user_id, post_id, content, created_at) VALUES (%s, %s, %s, %s)",
                    (user_id, post_id, comment_content, comment_created_at)
                )
                db_connection.commit()

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    create_fake_newsfeed_data()
    print("Fake newsfeed data created successfully!")
