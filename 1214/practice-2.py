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
                return jpy_rate

        print('找不到日圓匯率，請檢查來源網站')
        return None

    except Exception as e:
        print(f'取得匯率失敗 {e}')
        return None







