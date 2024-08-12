# manage.py

from flask import Flask
from config import Config
from app.views import post_views, user_views

app = Flask(__name__)
app.config.from_object(Config)

# Register the blueprint
app.register_blueprint(post_views)
app.register_blueprint(user_views)

if __name__ == '__main__':
    app.run()