from flask import Flask, request, jsonify
import sqlite3
import json

mirror = Flask(__name__)


@mirror.route('/', methods=['GET', 'POST'])
def echo():
    data = request.get_json()
    return jsonify({"result": "Success!", 'data': data})












if __name__ == "__main__":
    mirror.run(debug=True)
