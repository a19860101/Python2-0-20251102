import os
import urllib.request as req
import requests

url = 'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_052&keyword=&currency=TWD&sort=prec&page=2&start=0&count=10'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=header, verify=False)
res.encoding = 'utf-8'
json_file = res.json()

for i,data in enumerate(json_file['data']['data']):
    with open(f'kkday/{str(i)}/說明.txt','a', encoding='utf-8') as f:
        f.write(f'{data['name']}\n-----\n{data['introduction']}\n')
    for idx,img in enumerate(data['img_url_list']):
        # print(img)
        os.makedirs(f'kkday/{str(i)}', exist_ok=True)
        req.urlretrieve(img, f'kkday/{str(i)}/{str(idx)}.{os.path.basename(img)}')