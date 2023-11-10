"""
拿页面源代码
进行解析
"""
import requests
from lxml import etree

url = 'https://www.zbj.com/search/service/?l=0&kw=saas&r=1'
resp = requests.get(url)
# print(resp.text)
html = etree.HTML(resp.text)
divs = html.xpath('/html/body/div[2]/div/div/div[3]/div/div[3]/div[4]/div[1]/div')
print(divs)
