from flask import render_template, Response
from datetime import datetime
from time import sleep
from webseite import app


@app.route('/')
def index():
    return render_template('home/index.html', title='Home')


@app.route("/time/")
def time():
    def streamer():
        while True:
            yield "<p>{}</p>".format(datetime.now())
            sleep(1)

    return Response(streamer())