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
                return float(jpy_rate)

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
        manual = float(input('無法取得匯率，請手動輸入匯率或按 Enter 結束程式'))
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

    # 代購匯率
    custom_rate = float(input('請輸入代購匯率：'))

    # 3. 計算邏輯
    if is_tax:
        price_in_tax = price
        price_no_tax = price / (1 + tax_rate)
    else:
        price_no_tax = price
        price_in_tax = price * (1 + tax_rate)

    # print(f'含稅：{price_in_tax}')
    # print(f'未稅：{price_no_tax}')

    diff_jpy = round(price_in_tax - price_no_tax)

    twd_in_tax = round(price_in_tax * jpy_rate)
    twd_no_tax = round(price_no_tax * jpy_rate)
    # diff_twd = twd_in_tax - twd_no_tax
    diff_twd = round(diff_jpy * jpy_rate)
    print(f'日幣含稅：{price_in_tax}')
    print(f'日幣未稅：{price_no_tax:.0f}')
    print(f'日幣價差：{diff_jpy}')
    print(f'台幣含稅：{twd_in_tax}')
    print(f'台幣未稅：{twd_no_tax}')
    print(f'台幣價差：{diff_twd}')

    # 未稅成本(日幣) price_no_tax
    # 含稅成本(日幣) price_in_tax


    # 售價(台幣)
    product_price = round(price_in_tax * custom_rate)

    # 含稅購買到商品的利潤(台幣)
    profit_in_tax = product_price - twd_in_tax
    # 未稅購買到商品的利潤(台幣)
    profit_no_tax = product_price - twd_no_tax

    print(f'商品價格：{product_price}')
    print(f'含稅購買到的商品利潤：{profit_in_tax}')
    print(f'未稅購買到的商品利潤：{profit_no_tax}')

if __name__ == '__main__':
    main()