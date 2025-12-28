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

    name = input('商品名稱：')
    price = input('商品價格：')
    qty = input('商品數量：')

    sql = 'INSERT INTO products(name,price,qty)VALUES(%s,%s,%s)'
    data = [name, price, qty]
    cursor.execute(sql, data)
    conn.commit()

    print('資料新增成功!')

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
        print(product['name'])
        print(product['price'])
        print(product['qty'])
        print('#' * 30)
    cursor.close()
    conn.close()

def main():
    db_init()
    get_products()

if __name__ == '__main__':
    main()

