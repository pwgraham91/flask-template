import os

basedir = os.path.abspath(os.path.dirname(__file__))

# WTF
WTF_CSRF_ENABLED = True
SECRET_KEY = 'd5eadc6e-ee8a-4986-84f3-b34ca8730935'

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask_template'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


class Auth:
    CLIENT_ID = 'd5eadc6e-ee8a-4986-84f3-b34ca8730935.apps.googleusercontent.com'
    CLIENT_SECRET = 'd5eadc6e-ee8a-4986-84f3-b34ca8730935'
    REDIRECT_URI = 'http://template.ngrok.io/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'

ENVIRONMENT = 'dev'
