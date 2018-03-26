import flask
from flask_login import current_user

from app import app, login_manager
from app.models import User
from . import load_views


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    flask.g.user = current_user
