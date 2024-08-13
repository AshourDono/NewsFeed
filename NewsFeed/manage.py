# manage.py

from flask import Flask
from config import Config
from app.blueprints import post_blueprint, user_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Register the blueprint
app.register_blueprint(post_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run()