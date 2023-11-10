import requests  # 导入模块
import re
domain = 'https://www.dytt89.com/'
resp = requests.get(domain)
resp.encoding = 'gbk'  # 指定字符集
obj1 = re.compile(r'2022必看热片.*?<ul>(?P<name>.*?</ul>)', re.S)  # 正则表达
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'片　　名 (?P<movie>.*?)<br />.*?	<ul>		<li><a href="'
                  r'(?P<url1>.*?">)', re.S)
result = obj1.finditer(resp.text)
child_href_lst = []
for it in result:  # 拿到字符集
    for it1 in obj2.finditer(it.group('name')):  # 拿到网址
        child_href = domain + it1.group('href').strip('/')
    # print(child_href)
        child_href_lst.append(child_href)  # 拿到链接列表
# print(child_href_lst)
for href in child_href_lst:

    resp2 = requests.get(href)
    resp2.encoding = 'gb2312'
    # print(resp2.text)
    result_movie = obj3.finditer(resp2.text)
    for a in result_movie:
        print(a.group('movie'))

# 这个失败了