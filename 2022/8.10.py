# 屠戮电影天堂盗版电影
# 导入模块
import re
import requests

# 准备正则
obj1 = re.compile(r"2022必看热片.*?<ul>.*?(?P<url>.*?)</ul>", re.S)  # 获得字符集
obj2 = re.compile(r"<li><a href='(?P<child>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　(?P<name_movie>.*?)<.*?href="(?P<download>.*?)"', re.S)
child_lst = []  # 准备子链接列表
# 爬取网页
domain = 'https://www.dytt89.com/'
resp = requests.get(domain)
resp.encoding = 'gbk'
# print(resp.text)  # 测试网页是否爬取

# 爬取字符集
result1 = obj1.finditer(resp.text)
for a in result1:
    url = a.group('url')


# 爬取子链接

    result2 = obj2.finditer(url)
    for b in result2:
        child_url = (b.group('child'))  # 拿到裸子链接
        child = domain + child_url  # 拿到完整子链接
        child_lst.append(child)  # 将子链接拿到列表里
    # 进入子链接
    for item in child_lst:
        resp2 = requests.get(item)
        resp2.encoding = 'gbk'
        # print(resp2.text)  #  目前为止没有错误
        result3 = obj3.finditer(resp2.text)
        for c in result3:
            resp_name_movie = c.group('name_movie')
            resp_download = c.group('download')
            print(resp_name_movie)
            print(resp_download)  # 大功告成
