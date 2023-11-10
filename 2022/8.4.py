# # 翻译
# import requests
# url = "https://fanyi.baidu.com/sug"
# s = input('请输入你要翻译的内容')
# dic = {"kw": s}
# resp = requests.post(url, data=dic)
# print(resp.json())


# 豆瓣排行榜
import requests
url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}
ua = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
            '537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
}
resp = requests.get(url, params=param, headers=ua)
print(resp.json())
resp.close()
