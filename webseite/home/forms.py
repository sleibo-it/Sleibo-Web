from wtforms import Form, StringField, TextAreaField, EmailField, validators


class ContactForm(Form):
    Vorname = StringField('Vorname', [validators.Length(min=2, max=20)])
    Nachname = StringField('Nachname', [validators.Length(min=2, max=20)])
    email = EmailField(' Email', [validators.Length(min=5, max=30)])
    betreff = StringField('Betreff', [validators.Length(min=2, max=20)])
    nachricht = TextAreaField('Nachricht', [validators.Length(min=5, max=500)])

