import sqlite3
import json

# open json file
f = open('demo.json')
# return json object as a dict
data = json.load(f)

# Iterating through the json
# list
for i in data:
    print(i)

# Closing file
f.close()





