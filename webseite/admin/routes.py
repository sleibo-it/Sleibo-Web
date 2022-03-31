from flask import render_template, session, request, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm
from .models import User
from webseite.home.models import Contact
from webseite import app, db, bcrypt


@app.route('/admin')
def home():
    if 'username' not in session:
        flash(f'Bitte zuerst Anmelden', 'danger')
        return redirect(url_for('login'))
    contact = Contact.query.all()
    return render_template('admin/index.html', contact=contact, title="Admin Page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['username'] = form.username.data
            flash(f'Hallo {form.username.data}', 'success')
            return redirect(request.args.get('next') or url_for('home'))
        else:
            flash('Wrong Passwort! Please try again.', 'danger')

    return render_template('admin/login.html', form=form, title="Login Page")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(Vorname=form.Vorname.data,
                    Nachname=form.Nachname.data,
                    username=form.username.data,
                    strasse=form.strasse.data,
                    plz=form.plz.data,
                    ort=form.ort.data,
                    email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Hallo {form.Vorname.data} danke für die Registrierung', 'success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title='Registeration Page')


@app.route('/logout')
def logout():
    session.clear()

    return redirect(url_for('index'))