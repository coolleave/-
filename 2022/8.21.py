import requests
from lxml import etree


url = 'https://www.zbj.com/search/service/?l=0&kw=saas&r=1'
resp = requests.get(url)
html = etree.HTML(resp.text)  # 把网页交给etree去处理

divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
# xpath 路径去找到每一个区域

# 进入循环每一个所选区域
for div in divs:  # //*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div[1]/div[3]/div[1]/span
    price = div.xpath('./div[3]/div/span/text()')[0].strip('￥').strip('狂欢价:')  # 用相对路径找到价格
    title = div.xpath('./div[3]/a/text()')[0]  # 用索引把所需要的信息提出来作为字符
    com_name = div.xpath('./a/div[2]/div[1]/div/text()')[0]
    good_com0 = div.xpath('./div[3]/div[2]/div[1]/span/text()')[0]
    good_com1 = div.xpath('./div[3]/div[2]/div[1]/span/text()')[1]
    good_com = good_com0 + good_com1
    print(good_com)
