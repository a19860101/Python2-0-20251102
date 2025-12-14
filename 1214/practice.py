import requests
import bs4



price = int(input('請輸入金額：'))
is_tax = input('含稅還是未稅？（含稅輸入1，未稅輸入0）')
tax = int(input('消費稅為多少？（10%輸入10，8%輸入8）'))
# price = 1000
# is_tax = True
# tax = 10

#取得匯率
url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
res = requests.get(url)
result = res.text
htmlfile = bs4.BeautifulSoup(result, 'html.parser')
jpy = float(htmlfile.select_one('table tbody tr:nth-of-type(8) td:nth-of-type(3)').text)

if is_tax == '1':
    tax_in = price
    if tax == 10:
        tax_out = price / (1+tax/100)
    else:
        tax_out = price / (1+tax/100)


else:
    tax_out = price
    if tax == 10:
        tax_in = price * (1+tax/100)
    else:
        tax_out = price * (1+tax/100)


print(f'含稅價日幣為{tax_in:.0f}，台幣為{(tax_in * jpy):.0f}')
print(f'未稅價日幣為{tax_out:.0f}，台幣為{(tax_out * jpy):.0f}')
print(f'消費稅{tax}%')
print(f'日幣價差為{(tax_in - tax_out):.0f}，台幣價差為{((tax_in - tax_out) * jpy):.0f}')
