# manage.py

from flask import Flask
from app.views.post_views import post_views

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(post_views)

if __name__ == '__main__':
    app.run(debug=True)

