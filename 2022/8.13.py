import requests
import re

for a in range(200003, 200015):
    domain = 'http://121.26.242.250:8001/'
    obj = re.compile(r'<div align="center"><img src="(?P<download>.*?)"')
    url = f'http://121.26.242.250:8001/jxsxsxxd.asp?yzxh={a}%20%20&nj=2'
    resp = requests.get(url)
    resp.encoding = 'gb2312'
    result = obj.finditer(resp.text)

    for i in result:
        download = domain + i.group('download')
        resp2 = requests.get(download)
        name = i.group('download').split('\\')[-1]
        with open(f'../图片/{name}', 'wb') as f:
            f.write(resp2.content)
        print('over!')
print('allover')


