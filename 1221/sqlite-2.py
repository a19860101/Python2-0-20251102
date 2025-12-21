import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

sql_insert = 'INSERT INTO users(name, phone, email)VALUES("john","0987654321","asdf@gmail.com")'
cursor.execute(sql_insert)

conn.commit()
conn.close()