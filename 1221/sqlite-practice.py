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

def main():
    print('test')



if __name__ == '__main__':
    main()

