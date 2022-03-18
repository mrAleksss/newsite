import requests

res = requests.post('http://localhost:5000/api/add_message/1234', json={'name': 'Liza'})
if res.ok:
    print(res.json())
