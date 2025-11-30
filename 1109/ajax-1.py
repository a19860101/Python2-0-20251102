import urllib.request as req
import json
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

for i in range(10):
    url = f'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&keyword=&currency=TWD&sort=prec&page={i+1}&start=0&count=10'

    request = req.Request(url, headers=header)

    with req.urlopen(request) as res:
        result = res.read().decode('utf-8')

    json_data = json.loads(result)

    # print(json_data['data'])
    # print(json_data['data']['data'])

    for item in json_data['data']['data']:
        print(item['name'])