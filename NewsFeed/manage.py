# manage.py

from flask import Flask
from config import Config
from app.extensions import db_connection
# from app.views.post_views import post_views

app = Flask(__name__)
app.config.from_object(Config)

# Register the blueprint
# app.register_blueprint(post_views)

if __name__ == '__main__':
    app.run(debug=True)