import bs4
import requests
from selenium import webdriver
import time

url = 'https://github.com/a19860101/'

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'cookie': ''
}

# res = requests.get(url, headers=header)

# result = res.text

# htmlfile = bs4.BeautifulSoup(result, 'html.parser')

# ta = htmlfile.find('span', class_='AppHeader-context-item-label')

cookies = {}
# print(header['cookie'])
# print(header['cookie'].split(';'))

for cookie in header['cookie'].split(';'):
    # print(cookie)
    if '=' in cookie:
        name, value = cookie.strip().split('=')
        # print(name, value)
        cookies[name] = value

print(cookies)

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

for name, value in cookies.items():
    driver.add_cookie({
        'name': name,
        'value': value
    })

# for name, value in cookies.items():
#     print({
#         'name': name,
#         'value': value
#     })
time.sleep(10)

driver.refresh()
#
time.sleep(10)
#
driver.close()
