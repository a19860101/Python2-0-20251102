import sqlite3

# 建立資料庫連線，若資料庫不存在就自動建立
conn = sqlite3.connect('test.db')
# 建立指標
cursor = conn.cursor()
# 建立資料表
sql_create_table = '''
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT
    )
'''

cursor.execute(sql_create_table)

conn.close()

# sqlite 預覽網站
# https://sqliteviewer.app/

