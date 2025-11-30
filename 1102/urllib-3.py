import urllib.request as req
import bs4

url = 'https://www.mobile01.com/forumtopic.php?c=16'

header = {
    'Cookie': 'ak_bmsc=7F91AB731FC0810513C85158F7DBAAEA~000000000000000000000000000000~YAAQjNDdFx8kHi6aAQAAIHD+Qh1QRUqF1JSFyH8bVGEIYS/QmUuPASj+O0ZbaXKgMHEkI+mMjeoYQDci1cWqaCnks2+8tgMFLvcu3LVF37TgcDJpM2MQaMqbZDWJKt1tkZCVDXEYJ+Dp9XRltHV9q8e/fCggimxTttsMaASLuQcja8dbjDnB5ZaFzPitlUnp5d3zrYAfgj1yDOnU3eLRss138+pBMiBND06LGTZLFnqvVuQTBVbtWUnFcz+MVRO1idum2aIR1ITnB7xtCx6EGNzjby38GrKmpJlFfL1hhRY/YnCk/prTRJfCt2fScG+FPR26FJI73jnzVO6Mvu+bU4u6rX11QCctuNE9h/viroayKOZduePh32DJFBAjPdQSd+ciPXnKO3einzHSFJg=; _pubcid=5894cd8c-5d2d-4d0e-8f58-f75061e9359a; _pubcid_cst=zix7LPQsHA%3D%3D; ucf_uid=a64d52ba-ac09-4b03-8b65-895708aeafdb; _tfpvi=NjMzZjcwYmUtNTk4OS00YjcwLTljYjgtNDc3ZjAzZjZhOTVmIzItNQ%3D%3D; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%222da349c6-bb0c-4274-ac77-d13409fec1cd%5C%22%2C%5B1762060564%2C339000000%5D%5D%22%5D%5D%5D; _gcl_au=1.1.200095433.1762060565; cto_bundle=J9ROgV9BZHNuamlxeVVET3JTM3N4VGJvRVBHZEpYNTRLbXFEdWRLY0gxOW9mdnNlVEk0aWcyRDMlMkJwWGZBQ3k5ZiUyQjExRjQlMkJTJTJGdE81YUhKNWQxY0ViS1EyaDBhJTJGTDM2ZElYVmtTdXVPb0lJc01CQ0c1dEMlMkJXaEhWYnc5NENYT2FmVWFoWQ; cto_bidid=oQ1JaV9zQVVXV0tZMEZtSml2YlJzSlNrQjlvOWFRbnRyMmNua0xoaWg0RUFkaTJndFlRNEZuQUxMRmxhaTZ1NzNuTk15WFZHRTNoZUdMMVlpM1JJRnpOMEdLQSUzRCUzRA; _ga=GA1.1.1050843859.1762060565; FCNEC=%5B%5B%22AKsRol8jt8S1iSHN0W4jdrUe79dW5IZqYfQTS6dknSduu0Dz1T2cgDYeAFtxhw8qsx8l4NjgK_MjEodNFEe7VEDvwamH3fxW3p8vKyvR2cWF_5QmnhPrkFPkUzEveC1ZO7qPPWKxkA_sxRyUyeALxHEKo3oS7aRm0w%3D%3D%22%5D%5D; __gads=ID=217d9d97591a2cb7:T=1762060565:RT=1762060565:S=ALNI_MaCXs0Ogidu590znW0XjmHpwHdWhg; __gpi=UID=000012fe55eb71d8:T=1762060565:RT=1762060565:S=ALNI_MYq6ogNAKJietfTXskeZVuSNN5pJQ; __eoi=ID=dd4b7af355c819f4:T=1762060565:RT=1762060565:S=AA-AfjZXWburV-k96ntE8Doa8qJS; _ga_952J398MTY=GS2.1.s1762060564$o1$g0$t1762060566$j59$l0$h0; _ga_2MYKFYXMP7=GS2.1.s1762060564$o1$g0$t1762060566$j59$l0$h0; _ga_DCHTH48ZN2=GS2.1.s1762060565$o1$g0$t1762060566$j59$l0$h0; __retuid=b8ac265-5655-76f-a599-d1556982e7e7; __fpid=e244798c0c4e49f1d8ab5579f29abf90; __retfs=fSes-64fc3b11-628a-16e6-5887; __htid=b913749b-f1f1-42d9-b6a1-3edaf0521f09; _ht_em=1; nineyi_did=9b933268-e335-4644-b482-b927f849b94a; _ht_5aaa20=1; bm_sv=1F8100226D3337375EB28B6A7C032CE0~YAAQbuNH0iBHCy+aAQAAjYECQx2/bdVnpkhn7GnrTjMYmAy7xDUy9BtVLqeVvC1iE7QCvZ7SkVPhziwOuSVO5wLJC7FToEfFn1cfFaUHGFo2p0AOFWaQsg7zi7qfBHQRhAu8KSoZnDYQYTjcG5tp7QGlN2XHY1iMdo15ensHlzdNrmQdA0cU0vQboEYMHhZGmzNxLlJ0LqdTb80laQwfE2WArOQSAXIUgYj8YoMKiWYqnHIsIAoxcFZKwyj3XffxWK8=~1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

request = req.Request(url, headers=header)

# res = req.urlopen(request)

with req.urlopen(request) as res:

    result = res.read().decode('utf-8')

htmlfile = bs4.BeautifulSoup(result, 'html.parser')

titles = htmlfile.find_all('div', class_='c-listTableTd__title')

with open('output.txt', 'a', encoding='utf-8')as f:
    for title in titles:
        print(title.find('a').text)

        # f.write(f'{title.find('a').text} \n')

# res.close()

print(res.closed)