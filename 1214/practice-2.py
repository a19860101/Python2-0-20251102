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
            if 'JPY' in row.find('div', class_='visible-phone').text:
                jpy_rate = row.select('.rate-content-cash')[1].text
                time.sleep(2)
                return jpy_rate

        print('找不到日圓匯率，請檢查來源網站')
        return None

    except Exception as e:
        print(f'取得匯率失敗 {e}')
        return None


def main():
    # 1.取得日幣匯率
    print('正在取得匯率...')
    jpy_rate = get_jpy_rate()
    if not jpy_rate:
        manual = input('無法取得匯率，請手動輸入匯率或按 Enter 結束程式')
        if manual:
            jpy_rate = manual
        else:
            sys.exit()
    print(f'目前日幣匯率為{jpy_rate}')
    print('-' * 50)

    # 2. 輸入資料
    price = int(input('請輸入金額（日幣）：'))
    is_tax_input = input('金額是否含稅？（含稅輸入1，未稅輸入0）：')
    is_tax = (is_tax_input == '1')

    tax_rate_input = int(input('消費稅為多少？（10%輸入 10，8%輸入 8）：'))

    # 轉換匯率，如 10% -> 0.1、8% -> 0.08
    tax_rate = tax_rate_input / 100

    # 3. 計算邏輯
    if is_tax:
        price_in_tax = price
        price_no_tax = price / (1 + tax_rate)
    else:
        price_no_tax = price
        price_in_tax = price * (1 + tax_rate)

    print(f'含稅：{price_in_tax}')
    print(f'未稅：{price_no_tax}')


if __name__ == '__main__':
    main()