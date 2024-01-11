import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}


def get_urls():
    url = 'http://www.12z.cn/book/wuxiaxianxia/'
    # 发送GET请求获取页面内容
    resp = requests.get(url, headers=headers)
    print(resp)
    resp.encoding = 'gbk'
    # 使用lxml解析页面内容
    html = etree.HTML(resp.text)
    # print(resp.text)
    # 使用XPath选择所有的小说的链接
    urls = html.xpath('/html/body/div[5]/div[1]/div[1]/div[2]/div/div/ul/li/a/@href')
    print(urls)
    for i in urls:
        download(i)


def download(url):
    resp = requests.get('http://' + url, headers=headers)
    resp.encoding = 'gbk'
    html = etree.HTML(resp.text)
    download_url = html.xpath('//*[@id="djxz"]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a/@href')
    name = html.xpath('/html/body/div[5]/div/div[1]/div/div[1]/text()')
    with open(f'{name}.zip', 'wb') as w:
        w.write(requests.get('http://' + download_url, headers=headers).content)
        print(f'成功下载文件{name}')


if __name__ == '__main__':
    get_urls()
