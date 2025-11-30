import urllib.request as req
import json
# url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=b7df779e-71a6-4148-8379-5afbd441d803&limit=1000&sort=ImportDate%20desc&format=JSON'
url = 'https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=35&logType=5'
header = {

}

request = req.Request(url, headers=header)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

json_data = json.loads(result)

print(json_data)

for item in json_data:
    print(item['機構名稱'])
    print(item['電話'])

# print(json_data['records'])
# for item in json_data['records']:
#     print(item)