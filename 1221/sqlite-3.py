import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# sql_select = 'SELECT * FROM users'
# sql_select = 'SELECT name FROM users'
# sql_select = 'SELECT name,phone FROM users'
# sql_select = 'SELECT * FROM users WHERE name = "john"'
# sql_select = 'SELECT * FROM users WHERE name = ?'
# sql_select = 'SELECT * FROM users WHERE name = ? AND phone = ?'
sql_select = 'SELECT * FROM users WHERE name = ? OR phone = ?'


# datas = cursor.execute(sql_select,['123','123123123'])

sql_search = 'SELECT * FROM users WHERE name LIKE ? OR phone LIKE ?'
s = 'gmail'
datas = cursor.execute(sql_search, [f'%{s}%'])

for data in datas:
    print(data)

conn.close()
