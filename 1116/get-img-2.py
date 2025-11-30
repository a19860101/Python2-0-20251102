import requests
import bs4
import os
import urllib.request as req
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.tenlong.com.tw/zh_tw/recent'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=header)

htmlfile = bs4.BeautifulSoup(res.text, 'html.parser')

# html, xml  markup language 標記語言

# print(htmlfile.select('a.cover'))

# imgs = htmlfile.find_all('a',class_='cover')
#
# for img in imgs:
#     print(img.img)

imgs = htmlfile.select('a.cover img')
for img in imgs:
    # imgname = os.path.basename(img['src'])
    _, ext = os.path.splitext(img['src'])
    ext = ext[:4]
    fullname = _ + ext
    filename = os.path.basename(fullname)

    os.makedirs('images/tenlong2', exist_ok=True)

    req.urlretrieve(img['src'], f'images/tenlong2/{filename}')







