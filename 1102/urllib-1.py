import urllib.request as req
import bs4

url = 'https://www.ptt.cc/bbs/Baseball/index.html'

res = req.urlopen(url)

result = res.read().decode('utf-8')

htmlfile = bs4.BeautifulSoup(result, 'html.parser')

# print(htmlfile.find('title'))
# print(htmlfile.find('a'))
# print(htmlfile.find('div', class_='title'))
# print(htmlfile.find('a',id='logo'))

print(htmlfile.find_all('div', class_='title'))

data = htmlfile.find_all('div', class_='title')

for d in data:
    # print(d.find('a').text)
    print(d.text)