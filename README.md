# sleibo-web


## Installation

Bevor Ihr das Installiert auf euren Webserver bitte prüft ob dieser wsgi fähig oder aber Proxy unterstützt.
Es muss ebenfalls Python3 installiert sein.(Python 3.9 oder höher).

### Erste Schritte

Sollte das alles der fall sein erst mal die benötigten Bibliotheken installieren und ein virtual environment:

 `python3 -m venv ` 
 
danach unter Linux:
 
`./wasauchimmer-env/bin/activate`

und unter Windows:

`./wasauchimmer-env/bin/activate.bat`

oder mit der Powershell:

`./wasauchimmer-env/bin/activate.ps1`



Jetzt die Bibliotheken installieren:

`pip install -r requirements.txt`

nun könnt Ihr die Webanwendung schon mal Lokal starten:

Windows: `py app.py`

Linux: `python3 ./app.py`

### Apache2 Webserver mit mod_wsgi

Hier habt Ihr Glück da müsst Ihr nicht viel tun ausser in der config.wsgi die Pfade anzupassen.
Ist ziemlich selbsterklärend was wo wie eingetragen wird. Noch besser ist das Ihr das mit dem per Handstarten euch sparen könnt.

Ist aber nicht immer die Beste Idee. Bei SQLite3 Datenbanken rate ich davon ab weil es nicht funktionieren wird.
Solltet Ihr den weg aber gehen wollen benutzt MySQL oder ähnliches unter [SQLalchemy](https://www.sqlalchemy.org/) findet Ihr eine Anleitung dazu.

### Nginx Webserver als Proxy

Hier gibt es mehrere Wege um sich das per Hand starten zu sparen eine Möglichkeit wäre Ihr installiert gunicorn
das geht am einfachsten mit pip in der Shell.

    pip install gunicorn

Als Nächstes erstellen wir eine Datei, die als Einstiegspunkt für unsere Anwendung dient. Diese sagt dem Gunicorn-Server, wie die Interaktion mit der Anwendung erfolgt.
Diese nennen wir wsgi.py:

    from myproject import app

    if __name__ == "__main__":
        app.run()`


Nun können wir gunicorn starten:

    gunicorn --bind 0.0.0.0:5000 wsgi:app

Um zu testen, ob das ganze auch funktioniert gib in deinen Browser http://deine_server_ip:5000 ein.

Wenn alles richtig gemacht hast sollte jetzt die Webseite zusehen sein.

So da wir das alle nicht immer tippen wollen erstellen wir uns ein autostart.bat für Windows und kopieren uns das vorher eingetippte da rein
und speichern das. Nun machen wir eine Verküpfung davon und kopieren diese in die Autostart
Wo ihr das findet ab Windows 2016,2019, 2022 Server oder Windows 10 oder 11 könnt Ihr bei Google erfragen.

Nun wird es was tricky jetzt das ganze für Linux da müsste ich wohl etwas ausführlicher sein. Warum aber das Rad neu erfinden?
Es gibt eine sehr gute Anleitung auf [digitalocean](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04-de).
Eigentlich für Ubuntu aber was da funktioniert klappt auch auf Debian. Es ist auch nicht sinnvoll, wenn ich euch hier das von der Ursuppe an alles erkläre.
Das ist nicht der Sinn und es gibt Leute, die das besser können.

## Wo finde ich was ?

Ja das leidige Thema und bevor man mich mit unnötigen Fragen löchert hier eine kleine Übersicht

### Datenbank Modelle

Aufgrund dessen das auf dauer, wie schon vorbereitet, die Konfiguration in die config.py ausgelagert wird habe ich alle Datenbankmodelle 
im Verzeichniss webseite unter models.py. Das wirkt zuerst zwar etwas unübersichtlich aber durch die Kommentare ist klar erklärt welche Klasse für was ist.

Einige Modelle sind zwar schon vorbereitet aber noch nicht implementiert und müssen erstmal noch überdacht werden. Wie Datenbankmodelle aufgebaut werden ist ebenfalls unter [SQLalchemy](https://www.sqlalchemy.org/) 
zu finden. Ansonsten wenn Ihr drüber schaut, ist es relativ easy und leicht zu verstehen.

### Ordnerstruktur

Um nicht die Übersicht ganz zu verlieren sind alle Ordner nach funktion erstellt worden. So zum Beispiel ist im Ordner Home die Landingpage.
. In dem Ordner home findet man die routes.py, forms.py und noch eine überflüssige model.py. Im Ordner /templates/home die dazugehörigen HTML Dateien.

### Design/Aussehen ändern

Das Aussehen der Webseite könnt Ihr mit der Datei layout.html im Ordner templates nach euren bedürfnissen anpassen. Der Zeit wird Bootstrap 5 als 
CSS-Framework benutzt. Wenn Ihr lieber euer eigenes CSS nutzen wollt und eigne javascript Anwendungen könnt Ihr diese in webseite/static/css für Stylesheets und 
webseite/static/js für javascript nutze. Ich gehe davon aus das Ihr wisst was Ihr da macht. Ansonsten empfehle ich euch [Selfhtml](https://wiki.selfhtml.org/).

## Konfiguration

Wie schon erwähnt wird auf langer sicht die Konfiguration in die config.py ausgelagert aber zurzeit befindet sich die noch in webseite/__ ini __.py
Hier ist folgendes zu änder: 

    ...
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sleibo.db'
    app.config['SECRET_KEY'] = 'slngqenrgüeqrngüqerg4emddcbet'
    ...

Blueprints werden hier hinzugefügt:

    ...
    from webseite.home.routes import home
    app.register_blueprint(home)
    ...

Die Bibliothek flask-Admin ist nicht fix und ist nur ein platzhalter und kann ignoriert werden oder entfernt werden.

Wenn Ihr flask-admin nicht nutzen möchtet, muss folgendes aus der __ ini __.py entfernt werden:

    ...
    from flask_admin import Admin
    from flask_admin.contrib.sqla import ModelView
    ...
    admin = Admin(app)
    ...
    from webseite.models import Kunde, Team, Post, Anfragen
    admin.add_view(ModelView(Kunde, db.session))
    admin.add_view(ModelView(Team, db.session))
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Anfragen, db.session))
 

Die Bibliothek flask-mail wurde noch nicht implementiert und kann erstmal entfernt werden. Der spätere sinn, ist das darüber  
E-Mails aud dem Ticket bereich und den Anfragen aus dem Kontaktformular an den Webseitenbetreiber und Kunden automatisch gesendet werden.





