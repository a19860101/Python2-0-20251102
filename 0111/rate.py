import requests,bs4

def get_rate():
    url = 'https://rate.bot.com.tw/xrt/quote/l6m/JPY'
    res = requests.get(url)
    result = res.text
    htmlfile = bs4.BeautifulSoup(result, 'html.parser')

    # print(htmlfile)

    rates = htmlfile.select('tbody tr td:nth-of-type(4)')

    for rate in rates:
        print(rate.text)

def main():
    get_rate()

if __name__=='__main__':
    main()