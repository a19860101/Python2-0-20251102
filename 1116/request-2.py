import requests

url = 'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_052&keyword=&currency=TWD&sort=prec&page=2&start=0&count=10'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=header, verify=False)

json_file = res.json()

for data in json_file['data']['data']:
    print(data['name'])