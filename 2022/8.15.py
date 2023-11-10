# 今日干一中学生照片
import requests
from bs4 import BeautifulSoup

for a in range(200003, 200010):
    domain_url = 'http://121.26.242.250:8001/'
    url = f'http://121.26.242.250:8001/jxsxsxxd.asp?yzxh={a}%20%20&nj=2'
    resp = requests.get(url)  # 将网页解析出来
    resp.encoding = 'gbk'  # 处理乱码问题
    page = BeautifulSoup(resp.text, 'html.parser')  # 将网页交给b处理
    # 以上代码正常
    src = page.find('img').get('src')  # 找到img标签下的图片链接
    download = domain_url + src  # 将子网页恢复成完整链接
    resp2 = requests.get(download)  # 拿到子网页
    name = src.split("\\")[-1]  # 切割下来图片链接的最后学号作为图片名称
    with open(f'../图片/{name}', 'wb') as f:  # 写入名称
        f.write(resp2.content)
print('over!')


