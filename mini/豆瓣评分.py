import requests
import re
import csv
url = 'https://movie.douban.com/top250?start=0&filter='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                         '103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}
resp = requests.post(url, headers=headers)
obj1 = re.compile(r'" class="">.*?<span class="title">(?P<name>.*?)</span>'
                  r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;/&nbsp;.*?'
                  r'<span class="rating_num" property="v:average">(?P<mark>.*?)</span>', re.S)
result = obj1.finditer(resp.text)
for i in result:
    print(i.group('name', 'year', 'mark'))
with open('data.csv', mode='w')as f:
    cw = csv.writer(f)
    for i in result:
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        cw.writerow(dic.values())
print('over')
