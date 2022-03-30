import json
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    d = {"id": 4, "name": "Masha"}
    d1 = json.dumps(d)
    data = json.loads(d1)
    conn = sqlite3.connect("Alex.db")

    sql = "insert into fil(id,name) values(%d,'%s')" % (data['id'], data['name'])
    print(sql)
    conn.execute(sql)
    conn.commit()
    conn.close()
    print("done")






if __name__ == '__main__':
    app.run(debug=True)
