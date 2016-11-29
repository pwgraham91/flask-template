import flask

from app import app
from app.views.handlers.auth_handler import get_google_authorization_url


@app.route('/')
@app.route('/index')
def index():
    user = flask.g.user
    return flask.render_template('index.html',
                                 title='Home',
                                 user=user,
                                 auth_url=get_google_authorization_url())
