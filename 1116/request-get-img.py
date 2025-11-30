import requests
import bs4
import os

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
    os.makedirs('images/tenlong', exist_ok=True)

    filename = os.path.basename(fullname)
    print(fullname)
    img_data = requests.get(img['src'])
    #
    with open(f'images/tenlong/{filename}', 'wb') as f:
        f.write(requests.get(img['src']).content)
        # f.write(img_data.content)





