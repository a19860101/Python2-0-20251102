import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 刪除資料
# DELETE FROM 資料表 WHERE id=值
# sql_delete = 'DELETE FROM users WHERE id = 2'
sql_delete = 'DELETE FROM users'
cursor.execute(sql_delete)
# cursor.execute(sql_delete,[2])

conn.commit()
conn.close()