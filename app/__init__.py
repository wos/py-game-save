#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask
from cards import CARDS, PLAYERS

from flask import render_template, send_from_directory
import json

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


print(__name__)
app = create_app()


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/cards', methods=['GET', 'POST'])
def cards():
    return json.dumps({'cards' : CARDS, 'players': PLAYERS})

@app.route('/node_modules/<path:path>')
def send_node(path):
    print(path)

    p = os.path.abspath("../node_modules")
    print p
    # pass
    return send_from_directory('node_modules', path)

from app.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run()
