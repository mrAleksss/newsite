import sqlite3
import json


conn = sqlite3.connect("Alex.db")
conn.execute('''CREATE TABLE FIL

      (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

      NAME           TEXT    NOT NULL );''')
conn.commit()
conn.close()
