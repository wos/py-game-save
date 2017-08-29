#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, session, redirect, url_for
from flask import render_template, flash, send_from_directory
import json

app = Flask(__name__)

maincards = [
    {
        'id': 1,
        'name': 'Нагатинская',
        'color': '#4A148C',
        'side': 'dark'
    },
    {
        'id': 2,
        'name': 'Житная',
        'color': '#4A148C',
        'side': 'dark'
    },
    {
        'id': 3,
        'name': 'Варшавское шоссе',
        'color': '#9FA8DA',
        'side': 'light'
    },
    {
        'id': 4,
        'name': 'Огарева',
        'color': '#9FA8DA',
        'side': 'light'
    },
    {
        'id': 5,
        'name': 'Первая парковая',
        'color': '#9FA8DA',
        'side': 'light'
    },
    {
        'id': 6,
        'name': 'Полянка',
        'color': '#880E4F',
        'side': 'dark'
    },
    {
        'id': 7,
        'name': 'Сретенка',
        'color': '#880E4F',
        'side': 'dark'
    },
    {
        'id': 8,
        'name': 'Ростовская наб',
        'color': '#880E4F',
        'side': 'dark'
    },
    {
        'id': 9,
        'name': 'Вавилова',
        'color': '#E65100',
        'side': 'light'
    },
    {
        'id': 10,
        'name': 'Рублевское шоссе',
        'color': '#E65100',
        'side': 'light'
    },
    {
        'id': 11,
        'name': 'Смоленская',
        'color': '#E65100',
        'side': 'light'
    },
    {
        'id': 12,
        'name': 'Пушкинская',
        'color': '#e53935',
        'side': 'light'
    },
    {
        'id': 13,
        'name': 'Тверская',
        'color': '#e53935',
        'side': 'light'
    },
    {
        'id': 14,
        'name': 'Маяковская',
        'color': '#e53935',
        'side': 'light'
    },
    {
        'id': 15,
        'name': 'Грузинский вал',
        'color': '#FFEB3B',
        'side': 'light'
    },
    {
        'id': 16,
        'name': 'Смоленская плошадь',
        'color': '#FFEB3B',
        'side': 'light'
    },
    {
        'id': 17,
        'name': 'Новинский бульвар',
        'color': '#FFEB3B',
        'side': 'light'
    },
    {
        'id': 18,
        'name': 'Кутузовский проспект',
        'color': '#33691E',
        'side': 'dark'
    },
    {
        'id': 19,
        'name': 'Щусева',
        'color': '#33691E',
        'side': 'dark'
    },
    {
        'id': 20,
        'name': 'Гоголевский бульвар',
        'color': '#33691E',
        'side': 'dark'
    },
    {
        'id': 21,
        'name': 'Малая Бронная',
        'color': '#1A237E',
        'side': 'dark'
    },
    {
        'id': 22,
        'name': 'Арбат',
        'color': '#1A237E',
        'side': 'dark'
    },
    {
        'id': 23,
        'name': 'Казанская ж/д',
        'color': '#E0E0E0',
        'side': 'light'
    },
    {
        'id': 24,
        'name': 'Рижская ж/д',
        'color': '#E0E0E0',
        'side': 'light'
    },
    {
        'id': 25,
        'name': 'Ленинградская ж/д',
        'color': '#E0E0E0',
        'side': 'light'
    },
    {
        'id': 26,
        'name': 'Курская ж/д',
        'color': '#E0E0E0',
        'side': 'light'
    },
    {
        'id': 27,
        'name': 'Электростанция',
        'color': '#E0E0E0',
        'side': 'light'
    },
    {
        'id': 28,
        'name': 'Водоканал',
        'color': '#E0E0E0',
        'side': 'light'
    }
]

players = [
    {
        'id': 0,
        'name': 'Player 1'
    },
    {
        'id': 1,
        'name': 'Player 2'
    },
    {
        'id': 2,
        'name': 'Player 3'
    }
]

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


@app.route('/cards', methods=['GET', 'POST'])
def cards():
    return json.dumps({'cards' : maincards, 'players': players})


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0'
        # port=int(options.port)
        )
