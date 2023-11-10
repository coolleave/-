import requests
from lxml import etree


url = 'https://www.zbj.com/search/service/?l=0&kw=saas&r=1'
resp = requests.get(url)
html = etree.HTML(resp.text)

divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
for div in divs:  # //*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div[1]/div[3]/div[1]/span
    price = div.xpath('./div[3]/div/span/text()')
    name = div.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div[1]/div[3]/a/text()')
    print(price)
    print(name)
