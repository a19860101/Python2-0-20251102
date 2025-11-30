import requests
import bs4

url = 'https://www.ptt.cc/bbs/Baseball/index.html'

header = {
    'user-agent': '',
    'cookie': '',
    'accept': ''
}

res = requests.get(url, headers=header, verify=False)

print(res.text)

htmlfile = bs4.BeautifulSoup(res.text, 'html.parser')

print(htmlfile)

