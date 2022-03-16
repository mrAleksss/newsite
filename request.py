import requests

new_women = {'id': 1, 'name': 'Kristina'}
requests.post('http://127.0.0.1:5000/insert', json=new_women).json()