"""
总体思路
1、解析主页 拿到子链接
2、分析子链接，利用bs4解析拿到图片链接
3、下载图片
"""

import requests
from bs4 import BeautifulSoup


url = 'http://bizhi360.com/weimei/'
domain = 'http://bizhi360.com/'
resp = requests.get(url)
resp.encoding = 'utf-8'
main_page = BeautifulSoup(resp.text, 'html.parser')  # 将页面交给bs去处理
alist = main_page.find("ul").find_all("a")
# 第一个find是找到所需的区域所以不用find_all 后边的find_all是在所需要的区域内
# 再进行查找所有a标签
for a in alist:
    href = domain + a.get('href')  # 因为已经将页面交给bs所以这里直接用get获取所需要的属性就行
    # 到此正常
    resp1 = requests.get(href)
    resp1.encoding = 'utf-8'
    child_page = BeautifulSoup(resp1.text, 'html.parser')
    download = child_page.find_all('img', class_="img")
    for b in download:
        src = b.get('src')  # 用src标签拿到下载链接
        img_name = src.split('/')[-1]  # 切下来最后的片段做名字
        resp_img = requests.get(src)  # 拿到网页
        with open(f'../图片/{img_name}', 'wb')as f:  # 写入文件
            f.write(resp_img.content)
"""
这里简要总结一下 下载图片的方法 
1、用requests拿到网页
2、用with open的wb模式操作文件
3、用resp.content进行写入
至此，困扰了将近一周的下载图片之谜终于是解开了！
"""