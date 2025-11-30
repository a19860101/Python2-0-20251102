import urllib.request as req
import bs4
import os

url = 'https://www.lccnet.com.tw/lccnet'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}

request = req.Request(url, headers=header)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

htmlfile = bs4.BeautifulSoup(result, 'html.parser')

imgs = htmlfile.find_all('img')

for img in imgs:
    print(img['src'])

    # print(os.path.basename(img['src']))
    # print(os.path.splitext(img['src']))

    imgname = os.path.basename(img['src'])
    # _, ext = os.path.splitext(img['src'])

    os.makedirs('output', exist_ok=True)

    if img['src'][:4] == 'http':
        # req.urlretrieve(img['src'],f'output/{imgname}')
        pass
    else:
        req.urlretrieve(f'https://www.lccnet.com.tw{img['src']}',f'output/{imgname}')