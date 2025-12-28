import mysql.connector
# pip install mysql-connector-python

config = {
    'user': 'root',
    'password': '88888888',
    'host': '127.0.0.1',
    'database': 'lccnet'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        phone VARCHAR(50),
        email VARCHAR(50)
    )
'''

cursor.execute(create_table_query)

cursor.close()
conn.close()
