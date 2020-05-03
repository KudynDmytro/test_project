import datetime
import json
import os
import sqlite3
import string
import random

import requests

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def root():
    return 'hello'


@app.route('/gen_password')
def gen_password():
    par = str(request.args['digits'])
    try:
        length = int(request.args['length'])
        if 8 <= length <= 24:
            if par == 'yes':
                return ''.join([
                    random.choice(string.ascii_lowercase + string.digits)
                    for _ in range(length)
                ])
            elif par == 'no':
                return ''.join([
                    random.choice(string.ascii_lowercase)
                    for _ in range(length)
                ])
        else:
            return ''.join('The length of password can be only between 8 and 24')
    except ValueError:
        return ''.join('Length must be a number')


@app.route('/get-customers')
def get_customers():
    state = str(request.args['state'])
    city = str(request.args['city'])
    query = f'select * from customers where State = "{state}" and City = "{city}"'
    records = execute_query(query)
    return str(records)


def execute_query(query):
    db_path = '/home/dmitry/Downloads/Telegram Desktop/chinook.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    return records


@app.route('/get_unique')
def get_unique_name():
    query = 'select distinct FirstName from customers'
    records = execute_query(query)
    num = 0
    for _ in records:
        num += 1
    return str(num)


@app.route('/get_value')
def get_value():
    q = 'select UnitPrice * Quantity from invoice_items'
    rec = execute_query(q)
    return str(rec)


app.run(debug=True)
