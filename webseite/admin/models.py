from webseite import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Vorname = db.Column(db.String(30), unique=False, nullable=False)
    Nachname = db.Column(db.String(50), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    strasse = db.Column(db.String(80), unique=True, nullable=False)
    plz = db.Column(db.String(5), unique=True, nullable=False)
    ort = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False, default='profile.jpg')

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()