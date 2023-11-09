import requests
import re
from concurrent.futures import ThreadPoolExecutor


def down_onepage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'A''ppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/'
                             '114.0.1823.58'}
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    obj1 = re.compile(r'title:"(?P<name>.*?)".*?mp3:"(?P<url>.*?)"', re.S)
    groups = obj1.finditer(resp.text)
    for i in groups:
        name = i.group('name')
        url_mp3 = i.group('url')
        # print(i.group('name'), i.group('url'))
        resp1 = requests.get('http:' + url_mp3, headers=headers)
        f = open(f'./英语听力/{name}.mp3', mode='wb')
        f.write(resp1.content)
        print(f'{name}over!')
        resp1.close()
    resp.close()


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for a in range(63000, 63100):
            t.submit(down_onepage, url=f'https://www.xyybs.com/index.php?m=wap&a=show&ewm=1&catid=129&id={a}')
