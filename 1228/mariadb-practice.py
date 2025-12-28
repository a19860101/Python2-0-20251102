import mysql.connector

# 資料庫設定

config = {
    'user': 'root',
    'password': '88888888',
    'host': '127.0.0.1',
    'use_pure': True,
    'database': 'shop'
}

DB_NAME = 'shop'

def set_connection():
    return mysql.connector.connect(**config)

def db_init():
    conn = set_connection()
    cursor = conn.cursor()

    # 建立資料庫
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {config['database']}')
    cursor.execute(f'USE {config['database']}')

    # 建立商品資料表
    create_products_table = '''
        CREATE TABLE IF NOT EXISTS products(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            price VARCHAR(100),
            qty INT
        )
    '''
    cursor.execute(create_products_table)

    conn.commit()
    cursor.close()
    conn.close()

def create_product():
    conn = set_connection()
    # conn.database = DB_NAME
    cursor = conn.cursor()
    print('--新增商品(在商品名稱輸入q結束新增模式)--')
    while True:
        name = input('商品名稱：')
        if name == 'q':break
        price = input('商品價格：')
        qty = input('商品數量：')

        sql = 'INSERT INTO products(name,price,qty)VALUES(%s,%s,%s)'
        data = [name, price, qty]
        cursor.execute(sql, data)
        conn.commit()

        print('資料新增成功!')
        print('繼續新增，或在商品名稱輸入q結束新增模式')

    cursor.close()
    conn.close()
def get_products():
    conn = set_connection()
    # cursor = conn.cursor()
    cursor = conn.cursor(dictionary=True)
    sql = 'SELECT * FROM products'
    cursor.execute(sql)
    products = cursor.fetchall()
    for product in products:
        print(f'{product['id']:<3}|{product['name']:<20}|{product['price']:<10}|{product['qty']:<5}')
    cursor.close()
    conn.close()
def delete_product():
    conn = set_connection()
    cursor = conn.cursor()
    while True:
        get_products()
        pid = input('請輸入要刪除的商品ID，或輸入q退出')
        if pid == 'q': break
        sql = 'DELETE FROM products WHERE id = %s'
        cursor.execute(sql, [pid])
        conn.commit()
        print('刪除成功')
    cursor.close()
    conn.close()

def main():
    db_init()

    while True:
        print('--商品管理系統--')
        print('1. 顯示所有商品')
        print('2. 新增商品')
        print('3. 刪除商品')
        print('0. 結束程式')

        choice = input('請輸入選項(0-3)：')

        if choice == '1':
            get_products()
        elif choice == '2':
            create_product()
        elif choice == '3':
            delete_product()
        elif choice == '0':
            break
        else:
            print('無效輸入，請重新選擇')

    print('已退出商品管理系統')
if __name__ == '__main__':
    main()

