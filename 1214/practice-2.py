import sys
import time

import requests
import bs4

def get_jpy_rate():
    try:
        url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
        res = requests.get(url)
        result = res.text
        htmlfile = bs4.BeautifulSoup(result, 'html.parser')

        rows = htmlfile.select('tbody tr')

        for row in rows:
            if 'JPY123' in row.find('div', class_='visible-phone').text:
                jpy_rate = row.select('.rate-content-cash')[1].text
                time.sleep(2)
                return jpy_rate

        print('找不到日圓匯率，請檢查來源網站')
        return None

    except Exception as e:
        print(f'取得匯率失敗 {e}')
        return None


def main():
    # 取得日幣匯率
    print('正在取得匯率...')
    jpy_rate = get_jpy_rate()
    if not jpy_rate:
        manual = input('無法取得匯率，請手動輸入匯率或按Enter結束程式')
        if manual:
            jpy_rate = manual
        else:
            sys.exit()
    print(f'目前日幣匯率為{jpy_rate}')

if __name__ == '__main__':
    main()