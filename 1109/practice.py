import urllib.request as req
import bs4
import os
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['書名','原價','特價' ,'折扣'])

url = 'https://www.tenlong.com.tw/zh_tw/recent'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}

request = req.Request(url, headers=header)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

htmlfile = bs4.BeautifulSoup(result, 'html.parser')

imgs = htmlfile.find_all('img')
books = htmlfile.find_all('li',class_='single-book')

for book in books:
    title = book.find('strong',class_='title')
    price = book.find('del')
    sale = book.select('.pricing > * :not(del)')

    print(title.find('a').text)
    print(price.text)
    print(sale)

    ws.append([
        title.find('a').text,
        price.text
    ])

    
wb.save('tenlong.xlsx')
# for img in imgs:
#     try:
#         _,ext = os.path.splitext(img['src'])
#         ext = ext[:4]
#         fullname = _ + ext
#         imgname = os.path.basename(fullname)
#
#         os.makedirs('tenlong', exist_ok=True)
#
#         req.urlretrieve(fullname, f'tenlong/{imgname}')
#     except Exception as e:
#         print('發生錯誤',e)
#         pass

