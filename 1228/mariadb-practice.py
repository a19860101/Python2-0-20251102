import mysql.connector
from datetime import datetime, timezone
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
    now_utc = datetime.now()
    while True:
        get_products()
        pid = input('請輸入要刪除的商品ID，或輸入q退出')
        if pid == 'q': break
        # sql = 'DELETE FROM products WHERE id = %s'
        sql = '''
            UPDATE products SET deleted_at=%s WHERE id=%s
        '''
        cursor.execute(sql, [now_utc,pid])
        conn.commit()
        print('刪除成功')
    cursor.close()
    conn.close()
def update_product():
    conn = set_connection()
    cursor = conn.cursor(dictionary=True)
    get_products()
    now_utc = datetime.now()
    while True:
        product_id = input('請輸入要修改的ID，或輸入q退出')
        if product_id == 'q':
            break

        cursor.execute('SELECT * FROM products WHERE id = %s', [product_id])
        data = cursor.fetchone()

        print(data)
        if data is None:
            print('該ID不存在')
            break

        old_name = data['name']
        old_price = data['price']
        old_qty = data['qty']

        print(f'正在修改ID {product_id} 的資料')
        new_name = input('新名稱：')
        new_price = input('新價格：')
        new_qty = input('新數量：')

        final_name = new_name if new_name else old_name
        final_price = new_price if new_price else old_price
        final_qty = new_qty if new_qty else old_qty

        sql = '''
            UPDATE products SET name=%s,price=%s,qty=%s,updated_at=%s WHERE id=%s
        '''
        cursor.execute(sql, [final_name, final_price, final_qty,now_utc, product_id])
        conn.commit()

        print('資料已修改')
        cursor.close()
        conn.close()
def main():
    db_init()

    while True:
        print('--商品管理系統--')
        print('1. 顯示所有商品')
        print('2. 新增商品')
        print('3. 刪除商品')
        print('4. 更新商品')
        print('0. 結束程式')

        choice = input('請輸入選項(0-3)：')

        if choice == '1':
            get_products()
        elif choice == '2':
            create_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            update_product()
        elif choice == '0':
            break
        else:
            print('無效輸入，請重新選擇')

    print('已退出商品管理系統')
if __name__ == '__main__':
    main()

