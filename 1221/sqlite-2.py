import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 新增資料
# INSERT INTO 資料表名稱(欄位1,欄位2,...)VALUES(值1,值2,...)
# sql_insert = 'INSERT INTO users(name, phone, email)VALUES("john","0987654321","asdf@gmail.com")'
# cursor.execute(sql_insert)

sql_insert = 'INSERT INTO users(name, phone, email)VALUES(?,?,?)'
cursor.execute(sql_insert,['mary', '0987545545', 'asdfasdfsadf@gmail.com'])

conn.commit()
conn.close()