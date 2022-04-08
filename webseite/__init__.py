from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sleibo.db'
app.config['SECRET_KEY'] = 'slngqenrgüeqrngüqerg4jmddcbet'
login_manager = LoginManager(app)
login_manager.login_view = 'Kunde.login'
login_manager.login_message_category = 'info'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
admin = Admin(app)
mail = Mail(app)


from webseite.models import Kunde, Team, Post, Anfragen
admin.add_view(ModelView(Kunde, db.session))
admin.add_view(ModelView(Team, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Anfragen, db.session))

from webseite.home.routes import home
app.register_blueprint(home)
