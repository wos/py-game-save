#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask import render_template, send_from_directory

app = Flask(__name__)

@app.route('/node_modules/<path:path>')
def send_node(path):
    print(path)
    # pass
    return send_from_directory('node_modules', path)


# @app.route('/static/<path:path>')
# def send_node(path):
#     return send_from_directory('static', path)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/additem', methods=['GET', 'POST'])
def additem():
    error = None
    if request.method == 'POST':
        print(request.form['name'])

    return render_template('additem.html', error=error, form=request.form)



if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
        # port=int(options.port)
        )
