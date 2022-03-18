from flask import Flask, request, jsonify

mirror = Flask(__name__)


@mirror.route('/', methods=['GET', 'POST'])
def echo():
    data = request.get_json()
    return jsonify({"result": "Success!", 'data': data})



if __name__ == "__main__":
    mirror.run(debug=True)
