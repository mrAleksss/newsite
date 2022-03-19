import json
import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        f = open('demo.json')
        data = json.load(f)
        return jsonify({'data': data})


conn = sqlite3.connect('orders.db')
conn.execute(""" CREATE TABLE IF NOT EXISTS personage (
                                        id integer PRIMARY KEY,
                                        age integer,
                                        name text,
                                        powers text
                                    );""")


def save_data(data):

    for line in data:
        sql = "insert into personage(id,age,name,powers) values(%d,%d,'%s','%s')" % (
            line['id'], line['age'], line['name'], line['powers'])
        conn.execute(sql)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
