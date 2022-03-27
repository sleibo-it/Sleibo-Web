from flask import Flask, render_template
from sys import version

app = Flask(__name__)

from webseite.admin import routes