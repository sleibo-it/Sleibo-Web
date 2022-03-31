from wtforms import Form, BooleanField, StringField, PasswordField,EmailField, validators


class LoginForm(Form):
    # username = StringField('Username', [validators.Length(min=4, max=25)])
    username = StringField('Benutzer', [validators.Length(min=4, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])


class RegistrationForm(Form):
    Vorname = StringField('Vorname', [validators.Length(min=2, max=25)])
    Nachname = StringField('Nachname', [validators.Length(min=2, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    strasse = StringField('Straße inkl. Hausnummer', [validators.Length(min=4, max=25)])
    plz = StringField('Postleitzahl', [validators.Length(min=5, max=5)])
    ort = StringField('Ort', [validators.Length(min=5, max=25)])
    email = EmailField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')