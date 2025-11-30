import urllib.request as req
import ssl
url = 'https://www.imdb.com'

ssl._create_default_https_context = ssl._create_unverified_context

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}
request = req.Request(url, headers=header)

with req.urlopen(request) as res:
    result = res.read()
print(result)