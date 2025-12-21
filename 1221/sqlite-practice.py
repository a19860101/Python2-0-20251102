import sqlite3
from random import choice

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
        print('新增會員（在姓名輸入q以退回主選單）')
        name = input('請輸入姓名：')
        if name == 'q':
            break
        phone = input('請輸入電話：')
        email = input('請輸入email：')

        data = [name, phone, email]
        cursor.execute(sql, data)
        conn.commit()
        print('-'*60)

def get_all_users():
    sql = 'SELECT * FROM users'
    cursor.execute(sql)
    datas = cursor.fetchall()
    for data in datas:
        print(data)

def delete_user():
    get_all_users()
    sql = 'DELETE FROM users WHERE id = ?'
    while True:
        pid = input('請輸入要刪除的id（輸入q取消）：')
        if pid == 'q':
            print('退出刪除模式')
            break
        cursor.execute(sql, [pid])
        conn.commit()

        if cursor.rowcount > 0:
            print(f'ID {pid}已被刪除')
        else:
            print('該ID不存在')

def search_users():
    sql_search = 'SELECT * FROM users WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?'
    while True:
        query = input('請輸入關鍵字（輸入q取消）：')
        if query=='q':
            break
        cursor.execute(sql_search, [f'%{query}%', f'%{query}%', f'%{query}%'])

        print(cursor.rowcount)
        # if cursor.rowcount > 0:
        #     datas = cursor.fetchall()
        #     for data in datas:
        #         print(data)
        # else:
        #     print('找不到啦')

def main():
    check_create_table()
    while True:
        print('會員管理系統')
        print('=' * 60)
        print('1. 顯示所有資料')
        print('2. 新增會員')
        print('3. 移除會員')
        print('4. 關鍵字搜尋')
        print('q. 結束程式')
        print('=' * 60)
        choice = input('請輸入項目（1,2,3,q）：')

        if choice == '1':
            get_all_users()
        elif choice == '2':
            create_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            search_users()
        elif choice == 'q':
            break
        else:
            print('無效輸入，請重新選擇')

    print('='*60)
    print('滾，程式結束')
    print('='*60)

    conn.close()

if __name__ == '__main__':
    main()

