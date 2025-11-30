import urllib.request as req

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

header = {
    'Cookie' : '_gid=GA1.2.1433470687.1762055211; cf_clearance=i9.mtC427HU7U2nDiZ2aB.UNS_dsUkT4Q3odHJuaKZE-1762055226-1.2.1.1-CHhk_wNyVTh8afFmnOzJEzsx7Zt6gKp557Ml7_BpzVsoCyYwsDTOFwvT73JsY.YbYL7hzCrgxUyhWwoVkG2M6BA9QPafupZ9aA_4gDQW0fecn_lI4bt9339yOMFcCM68hvPlTBGunU7IrYMVwcrAGKHyJLkiLYqvh834lxdhi_eAPYOr9WP6UD2y_6D4Jilu57gWAQha4XuJIPGTvxA_bQOG._i2vOmSH4uwYYVfTqQ; over18=1; _ga_DZ6Y3BY9GW=GS2.1.s1762055211$o1$g1$t1762055402$j59$l0$h0; _ga=GA1.2.766531258.1762055211; _gat=1'
}

request = req.Request(url, headers=header)

res = req.urlopen(request)

result = res.read().decode('utf-8')

print(result)