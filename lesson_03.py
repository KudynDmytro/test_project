import csv
from flask import Flask

from faker import Faker

app = Flask(__name__)


@app.route('/read_file')
def read_file():
    with open('requirements.txt', 'r') as f:
        data = f.read()
        return data


# read_file()

@app.route('/fake_info')
def fake_info():
    fake = Faker()

    for _ in range(1, 101):
        print(_, fake.name(), fake.email())


# fake_info()


@app.route('/read_data_from_csv')
def read_data_from_csv(filepath):

    with open(filepath, "r") as f:
        rows = [row for row in csv.DictReader(f)]

    return rows


rows = read_data_from_csv('hw.csv')


@app.route('/sort_height')
def sort_height():
    height = []
    for row in rows:
        height.append(float(row[' \"Height(Inches)\"']))
    return height


sort_height()


@app.route('/sort_weight')
def sort_weight():
    weight = []
    for row in rows:
        weight.append(float(row[' \"Weight(Pounds)\"']))
    return weight


@app.route('/avg')
def avg(h, w):
    r = open('hw.csv', 'r')

    data_size = 0
    for i in r:
        if i[0].isnumeric():
            data_size += 1

    h_sum = 0
    for k in h:
        h_sum += k

    w_sum = 0
    for g in w:
        w_sum += g

    w_avg = (w_sum / data_size) * 0.453

    h_avg = (h_sum / data_size) * 2.54

    r.close()

    return h_avg, w_avg


print(avg(sort_height(), sort_weight()))


