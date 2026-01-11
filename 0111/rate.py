import requests,bs4,json
import mysql.connector

config = {
    'user': 'root',
    'password': '88888888',
    'host': '127.0.0.1',
    'use_pure': True,
    'database': 'lccnet'
}

# 1. 剛剛發行的 Channel Access Token (長的那串)
TOKEN = ""
# 2. 你的 User ID (U開頭的那串)
USER_ID = "U70fb069f9dfe9dd357bf725513c81514"

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

def show_rates():
    conn = set_connection()
    cursor = conn.cursor(dictionary=True)
    sql = 'SELECT * FROM rates'
    cursor.execute(sql)
    rates = cursor.fetchall()

    rate_str = ''
    for rate in rates[:30]:
        # print(rate['date'],rate['jpy'])
        rate_str += rate['date'] + ':' + rate['jpy'] + '\n'

    conn.commit()
    cursor.close()
    conn.close()

    return rate_str

def send_msg(msg):
    # 傳送的訊息
    # text = "嘿嘿嘿!"
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + TOKEN
    }
    payload = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": msg}]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print("成功！！")
        else:
            print(f"失敗: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"錯誤: {e}")

def main():
    db_init()
    send_msg(show_rates())
    # show_rates()
    # save_rates_to_data()
if __name__=='__main__':
    main()
    # input("程式執行結束，請按 Enter 鍵離開...")

# pyinstaller -F --hidden-import=mysql.connector.plugins.mysql_native_password 你的檔名.py