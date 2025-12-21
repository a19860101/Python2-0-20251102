import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 查詢資料
sql_select = 'SELECT * FROM users'
# sql_select = 'SELECT name FROM users'
# sql_select = 'SELECT name,phone FROM users'
# sql_select = 'SELECT * FROM users WHERE name = "john"'
# sql_select = 'SELECT * FROM users WHERE name = ?'
# sql_select = 'SELECT * FROM users WHERE name = ? AND phone = ?'
# sql_select = 'SELECT * FROM users WHERE name = ? OR phone = ?'


# datas = cursor.execute(sql_select)
# datas = cursor.execute(sql_select,['123','123123123'])
# cursor.execute(sql_select)
# datas = cursor.fetchall()

# 模糊比對
sql_search = 'SELECT * FROM users WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?'
s = 'gmail'
cursor.execute(sql_search, [f'%{s}%',f'%{s}%', f'%{s}%'])
datas = cursor.fetchall()

for data in datas:
    print(data)

print('+'*50)

for data in datas:
    print(data)

conn.close()
