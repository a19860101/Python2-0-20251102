import sqlite3

# 建立資料庫連線，若資料庫不存在就自動建立
conn = sqlite3.connect('test.db')
# 建立指標
cursor = conn.cursor()
# 建立資料表
sql_create_table_1 = '''
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT
    )
'''

# 建立資料表如果資料表不存在
sql_create_table = '''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT
    )
'''

cursor.execute(sql_create_table)

# 新增欄位
sql_add_col = 'ALTER TABLE users ADD COLUMN address TEXT'
# cursor.execute(sql_add_col)

# 移除欄位
sql_drop_col = 'ALTER TABLE users DROP COLUMN address'
# cursor.execute(sql_drop_col)

# 修改欄位
sql_rename_col = 'ALTER TABLE users RENAME account TO name'
# cursor.execute(sql_rename_col)

# 修改資料表名稱
sql_rename_table = 'ALTER TABLE students RENAME TO users'
# cursor.execute(sql_rename_table)

conn.close()

# sqlite 預覽網站
# https://sqliteviewer.app/

