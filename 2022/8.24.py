"""
今日爬取网易云音乐评论
可能比较难
加油冲冲冲
首先也是要拿到网页
然后看看在不在源代码里
if在就直接用re bs4 xpath直接去解析就行
elif不在就通过浏览器的抓包工具去抓
大体思路就是这样 开始咯

"""

# 导入模块
import requests


url = 'https://music.163.com/#/song?id=1808492017'

resp = requests.get(url)
print(resp.text)