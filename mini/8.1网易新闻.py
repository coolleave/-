import requests
from lxml import etree
import uuid  # 导入生成随机数

url = 'https://www.163.com/dy/article/IAOKF1AJ0514R9P4.html'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}
resp = requests.get(url, headers=headers)
tree = etree.HTML(resp.text)
# print(tree)
div = tree.xpath('//div[@class="post_body"]')[0]
print(div)

page = etree.tostring(div, encoding='utf-8').decode('utf-8')  # 将div转化为源码格式
# print(page)
srcs = div.xpath(".//img/@src")
for src in srcs:
    img_name = str(uuid.uuid4()).replace('_', '') + '.jpg'
    resp = requests.get(src)
    with open(img_name, mode='wb') as f:
        f.write(resp.content)
    page = page.replace(src, img_name)  # 将网上的路径转化为本地图片路径
with open('新闻.md', mode='w', encoding='utf-8') as f:  # 写入markdown格式，有图有文字
    f.write(page)
