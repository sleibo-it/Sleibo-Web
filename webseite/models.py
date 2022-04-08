from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from webseite import db, login_manager
import platform
import os


@login_manager.user_loader
def load_kunde(kunde_id):
    return Kunde.query.get(int(kunde_id))


@login_manager.user_loader
def load_team(team_id):
    return Team.query.get(int(team_id))


#  -------User and roles Beginn ---------

class Kunde(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Vorname = db.Column(db.String(30), unique=False, nullable=False)
    Nachname = db.Column(db.String(50), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    strasse = db.Column(db.String(80), unique=True, nullable=False)
    plz = db.Column(db.String(5), unique=True, nullable=False)
    ort = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile_img = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')

    def __repr__(self):
        return f"Kunde('{self.username}', '{self.email}', '{self.profile_img}')"

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'kunde_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            kunde_id = s.loads(token)['kunde_id']
        except:
            return None
        return Kunde.query.get(kunde_id)

    def __repr__(self):
        return f"Kunde('{self.username}', '{self.email}', '{self.image_file}')"


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent = db.Column(db.Integer, autoincrement=True, unique=True, nullable=False)
    Vorname = db.Column(db.String(30), unique=False, nullable=False)
    Nachname = db.Column(db.String(50), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    strasse = db.Column(db.String(80), unique=True, nullable=False)
    plz = db.Column(db.String(5), unique=True, nullable=False)
    ort = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile_img = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')

    def __repr__(self):
        return f"Team('{self.username}', '{self.email}', '{self.profile_img}')"


#  -------User and roles End---------
#  -------Content Begin---------

# TODO: Schnellst möglich fertig stellen
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __repr__(self):
        return f"Contact('{self.title}', '{self.date_posted}')"


#  -------Content End---------
# -------Customer Service Begin -------
class Anfragen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Vorname = db.Column(db.String(30), nullable=False)
    Nachname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    betreff = db.Column(db.String(20), nullable=False)
    nachricht = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"Anfragen('{self.title}', '{self.date}')"


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticketnumber = db.Column(db.Integer, autoincrement=True, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date_ticket = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    kunde_id = db.Column(db.Integer, db.ForeignKey('kunde.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_ticket}')"


# -------Customer Service End -------
# -------Shop Begin -------
# TODO: Shop eilt zar nicht aber mal zumindest gdenken drum machen was man für die Datenbank dafür benötigt

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class AddProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    color = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pup_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    brand_id = db.Column(db.Integer, db.ForeignKey(Brand.id), nullable=False)
    brand = db.relationship('Brand', backref=db.backref('brands', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))

    images_1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    images_2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    images_3 = db.Column(db.String(150), nullable=False, default='image.jpg')

    def __repr__(self):
        return '<Addproduct \r>' % self.name


# -------Shop End -------


db.create_all()
