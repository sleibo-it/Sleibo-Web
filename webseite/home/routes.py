from flask import render_template, Response, request,  redirect, url_for
from .forms import ContactForm
from .models import Contact
from webseite import app, db


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home/index.html', title='Home')


@app.route('/impressum/')
def impressum():
    return render_template('home/impressum.html', title='Impressum')


@app.route('/contact', methods=['GET', 'POST'])
def get_contact():
    form = ContactForm(request.form)
    # here, if the request type is a POST we get the data on contat
    # forms and save them else we return the contact forms html page
    if request.method == 'POST' and form.validate():
        nachricht = Contact(Vorname=form.Vorname.data,
                            Nachname=form.Nachname.data,
                            email=form.email.data,
                            betreff=form.betreff.data,
                            nachricht=form.nachricht.data)
        db.session.add(nachricht)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('home/contact.html', form=form, title='Kontakt')


