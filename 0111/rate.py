import requests,bs4
import mysql.connector

config = {
    'user': 'root',
    'password': '88888888',
    'host': '127.0.0.1',
    'use_pure': True,
    'database': 'lccnet'
}
def set_connection():
    return mysql.connector.connect(**config)

def db_init():
    conn = set_connection()
    cursor = conn.cursor()

    # 建立資料庫
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {config['database']}')
    cursor.execute(f'USE {config['database']}')

    # 建立商品資料表
    create_rates_table = '''
        CREATE TABLE IF NOT EXISTS rates(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date VARCHAR(100),
            jpy VARCHAR(100)
        )
    '''
    cursor.execute(create_rates_table)

    conn.commit()
    cursor.close()
    conn.close()

def get_rate():
    url = 'https://rate.bot.com.tw/xrt/quote/l6m/JPY'
    res = requests.get(url)
    result = res.text
    htmlfile = bs4.BeautifulSoup(result, 'html.parser')

    # print(htmlfile)

    datas = []

    # rates = htmlfile.select('tbody tr td:nth-of-type(4)')
    rates = htmlfile.select('tbody tr')
    for rate in rates[:30]:
        # print(rate.select('td'))
        result = rate.select('td')
        # print(result[0].text)
        # print(result[3].text)
        datas.append([result[0].text,result[3].text])

    return datas

def save_rates_to_data():
    conn = set_connection()
    cursor = conn.cursor()
    cursor.execute('TRUNCATE TABLE rates')
    sql = 'INSERT INTO rates(date,jpy)VALUES(%s,%s)'
    cursor.executemany(sql, get_rate())
    print('匯率已存入資料庫')
    conn.commit()
    cursor.close()
    conn.close()

def main():
    db_init()
    # get_rate()
    save_rates_to_data()

if __name__=='__main__':
    main()