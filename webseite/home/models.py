from webseite import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Vorname = db.Column(db.String(30), nullable=False)
    Nachname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    betreff = db.Column(db.String(20), nullable=False)
    nachricht = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<betreff \r>' % self.betreff


db.create_all()