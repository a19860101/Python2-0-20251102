import mysql.connector
# pip install mysql-connector-python

config = {
    'user': 'root',
    'password': '88888888',
    'host': '127.0.0.1',
    'database': 'lccnet',
    'use_pure': True
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

sql = 'SELECT * FROM users'

cursor.execute(sql)

data = cursor.fetchall()

# print(data)

for user in data:
    print(user)
    # print(user[0])
    # print(user[1])
    # print(user[2])
    # print(user[3])
    print('-' * 20)

cursor.close()
conn.close()