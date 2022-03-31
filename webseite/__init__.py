from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sleibo.db'
app.config['SECRET_KEY'] = 'slngqenrgüeqrngüqerg4jmddcbet'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from webseite.home import routes
from webseite.admin import routes