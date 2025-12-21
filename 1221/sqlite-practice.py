import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

def check_create_table():
    sql_create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone TEXT,
        email TEXT
        )
    '''
    cursor.execute(sql_create_table)

def create_user():
    sql = 'INSERT INTO users(name, phone, email)VALUES(?,?,?)'
    while True:
        name = input('請輸入姓名')
        if name == 'q':
            break
        phone = input('請輸入電話')
        email = input('請輸入email')

        data = [name, phone, email]
        cursor.execute(sql, data)
        conn.commit()

def get_all_users():
    sql = 'SELECT * FROM users'
    cursor.execute(sql)
    datas = cursor.fetchall()
    for data in datas:
        print(data)




def main():
    print('test')




if __name__ == '__main__':
    main()

