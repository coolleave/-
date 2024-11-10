import requests
import json


def getUrl():
    url = 'https://shop.gitapp.cn/api/myapp/index/thing/list'
    res = requests.get(url).content
    res = res.decode('utf-8')
    res_json = json.loads(res)
    items = res_json['data']
    for item in items:
        # print(item['cover'])
        print("__________________________")
        # /upload/cover/1679230364390.jpeg
        # https://shop.gitapp.cn/api//upload/cover/1679403403756.jpeg
        admin_url = 'https://shop.gitapp.cn/api/'
        pic_url = admin_url + item['cover']
        name = item['id']
        download_pic(name, pic_url)


def download_pic(id, url):
    resp = requests.get(url)
    # 将图片保存到本地文件
    with open(f'pic/{id}.jpg', 'wb') as file:
        file.write(resp.content)
        print(f"图片已成功下载并保存到 pic/{id}")


if __name__ == '__main__':
    getUrl()
