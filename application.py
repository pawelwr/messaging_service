import os

from flask import Flask
from flask_socketio import SocketIO, emit

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)


@app.route("/")
def index():
    return "Project 2: TODO"
