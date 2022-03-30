import json
import sqlite3


def sql_json():
    with open("sample.json", 'r') as f:
        data = json.load(f)
        conn = sqlite3.connect("Alex.db")

        sql = "insert into fil(id,name) values(%d,'%s')" % (data['id'], data['name'])
        print(sql)
        conn.execute(sql)
        conn.commit()
        conn.close()
        print("done")


sql_json()
