import requests
import bs4

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

res = requests.get(url)

result = res.text

htmlfile = bs4.BeautifulSoup(result, 'html.parser')

jpy = htmlfile.select_one('table tbody tr:nth-of-type(8) td:nth-of-type(3)')
usd = htmlfile.select_one('table tbody tr:nth-of-type(1) td:nth-of-type(3)')
krw = htmlfile.select_one('table tbody tr:nth-of-type(16) td:nth-of-type(3)')

print(jpy.text)
print(usd.text)
print(krw.text)