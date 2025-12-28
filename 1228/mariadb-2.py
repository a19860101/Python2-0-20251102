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

name = input('姓名')
phone = input('電話')
email = input('Email')

create_user_query = 'INSERT INTO users(name,phone,email)VALUES(%s,%s,%s)'
# cursor.execute(create_user_query, ['John','0987654321','john@gmail.com'])
cursor.execute(create_user_query, [name, phone, email])

# data = [
#     ('John1','0987654321','john@gmail.com'),
#     ('John2','0987654321','john@gmail.com'),
#     ('John3','0987654321','john@gmail.com'),
#     ('John4','0987654321','john@gmail.com'),
# ]

# cursor.executemany(create_user_query, data)

conn.commit()

cursor.close()
conn.close()