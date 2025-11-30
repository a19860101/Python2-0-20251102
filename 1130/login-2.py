import bs4
import requests

url = 'https://github.com/a19860101/'

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'cookie':''
}

res = requests.get(url, headers=header)

result = res.text

htmlfile = bs4.BeautifulSoup(result, 'html.parser')

ta = htmlfile.find('span', class_='AppHeader-context-item-label')

print(ta)