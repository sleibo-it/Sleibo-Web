from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from webseite.config import Config
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_security import Security


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
basic_auth = BasicAuth()
mail = Mail()
admin = Admin()
security = Security()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # flask-admin
    admin.init_app(app)

    # flask-BasicAuth
    # basic_auth = BasicAuth(app)

    # flask-admin Anfang
    from webseite.models import User, Post
    from flask_admin.contrib.sqla import ModelView
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    # flask-admin Ende

    # flask-BasicAuth Anfang

    # flask-BasicAuth Ende

    # Blueprints Anfang
    from webseite.users.routes import users
    from webseite.posts.routes import posts
    from webseite.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    # Blueprints Ende

    return app
