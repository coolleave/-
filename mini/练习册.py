import requests

for a in range(1, 100):
    url = f'https://book.yunzhan365.com/suls/pnai/files/mobile/{a}.jpg'
    resp = requests.get(url)
    with open(f'../图片/{a}.jpg', mode='wb') as f:
        f.write(resp.content)
print('over!')
