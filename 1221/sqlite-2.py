import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 新增資料
# INSERT INTO 資料表名稱(欄位1,欄位2,...)VALUES(值1,值2,...)
# sql_insert = 'INSERT INTO users(name, phone, email)VALUES("john","0987654321","asdf@gmail.com")'
# cursor.execute(sql_insert)

sql_insert = 'INSERT INTO users(name, phone, email)VALUES(?,?,?)'
while True:
    name = input('請輸入姓名')
    if name == 'q':
        break

    phone = input('請輸入電話')
    email = input('請輸入email')


    data = [name, phone, email]
    cursor.execute(sql_insert,data)

# datas = [
#     ('mary2', '0987654321', 'asdf2@gmail.com'),
#     ('mary3', '0987654321', 'asdf2@gmail.com'),
#     ('mary4', '0987654321', 'asdf2@gmail.com'),
#     ('mary5', '0987654321', 'asdf2@gmail.com'),
# ]
# cursor.executemany(sql_insert,datas)


    conn.commit()

conn.close()