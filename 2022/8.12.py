# bs4的安装
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple bs4

# import requests
# url = 'http://121.26.242.250:8001/zpk/200407.jpg'
# resp = requests.get(url)
# print(resp)
# 又一次猜想失败

# 搞搞菜价
import requests
from bs4 import BeautifulSoup
# 拿到网页源码
url = 'http://www.xinfadi.com.cn/index.html'
resp = requests.get(url)
# 讲页面交给bs4处理 拿到对象
page = BeautifulSoup(resp.text, 'html.parser')
# 从bs4中解析数据
table = page.find("table", attrs={'border': "0"})
trs = table.find_all('tr')[1:]
for i in trs:
    tds = i.find_all('td')
    name = tds[0].text
    print(name)
