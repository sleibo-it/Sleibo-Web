from flask import render_template, Response, request,  redirect, url_for
from datetime import datetime
from .forms import ContactForm
from .models import Contact
from webseite import app, db



@app.route('/')
def index():
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
    return render_template('home/index.html', form=form, title='Home')


@app.route('/impressum/')
def impressum():
    return render_template('home/impressum.html', title='Impressum')


'''
@app.route('/contact', methods=['GET', 'POST'])
def get_contact():
    form2 = ContactForm(request.form)
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
    return render_template('home/contact.html', form=form2, title='Kontakt')
'''

