# import requests
# from lxml import etree
#
# # url = 'http://121.26.242.250:8001/srcja.asp?dhhm1=aaaa'
# # resp = requests.get(url)
# # resp.encoding = 'gbk'
# # print(resp.text)
# # # /html/body/table/tbody/tr[3]/td/table/tbody/tr/td[4]/div/font/img
# # html = etree.HTML(resp.text)
# # div = html.xpath('/html/body/table/tbody/tr[3]/td/table/tr/form/td[4]/div/font/img/@src')
# # print(div)
# # # 上面除了点小插曲，困扰了两天，由于浏览器处理的时候会优化补充网页源代码 所以使用浏览器复制的xpath会出问题
# # # 一定要去源码中看好在进行写xpath
#
# url = 'https://www.zbj.com/search/service?r=1&kw=saas&l=1'
# resp = requests.get(url, User-Agent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54')
# print(resp.text)
# html = etree.HTML(resp.text)
# # /html/body/div[2]/div/div/div[3]/div/div[3]/div[4]/div[1]/div[1]/@class
# # //*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div[1]
# divs = html.xpath('/html/body/div/div//span/@data-adlinkid="" ')
# print(divs)

# 重新开始
import requests
from lxml import etree
url = 'https://www.proginn.com/search?keyword=saas'
dic = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54'}
resp = requests.get(url, headers=dic)
tree = etree.HTML(resp.text)  # 将网页交给etree来解析
divs = tree.xpath('/html/body/div[2]/div[3]/div')
for div in divs:
    name = div.xpath('.//div[2]/div[1]/a/span/text()')
    print(name)
