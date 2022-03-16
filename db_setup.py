import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS women(women_id INTEGER PRIMARY KEY, name TEXT);")
conn.commit()
conn.close()
