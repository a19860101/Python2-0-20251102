import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

sql_create_table = '''
CREATE TABLE users
    (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT
    )
'''

cursor.execute(sql_create_table)

conn.close()

