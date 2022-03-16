from flask import Flask, request

mirror = Flask(__name__)
new_women = {'id': 1, 'name': 'Kristina'}


@mirror.route('/', methods=['POST'])
def example():
    return {'success': True, 'new_women': request.json}


print(new_women)
