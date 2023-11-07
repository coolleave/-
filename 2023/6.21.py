from lxml import etree
import requests

url = 'https://www.leleketang.com/let3/knowledges.php?grade_id=30'
# 请求网页
resp = requests.get(url)
# 调整字符编码
resp.encoding = 'utf-8'
# 尝试打印网页内容
print(resp.text)
# 把网页交给etree处理
tree = etree.HTML(resp.text)
name = tree.xpath('/html/body/div/div/div/div[4]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/a/text()')
print(name)
