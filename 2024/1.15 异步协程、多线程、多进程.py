import asyncio
import threading
import requests
from lxml import etree
import random
from concurrent.futures import ThreadPoolExecutor


# 定义函数
def test1():
    for a in range(1000):
        print(a, '线程')


def test2():
    t = threading.Thread(target=test1())  # 创建线程
    t.start()  # 线程可以执行了，具体时间由cpu决定
    for i in range(1000):
        print(i, '主线程')


# 线程池
with open('../../项目/代理ip池.txt', 'r', encoding='utf-8') as r:
    ip = r.read()
    lst_ip = eval(ip)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}


def simple_down(url):
    resp = requests.get('http://www.12z.cn' + url, headers=headers, proxies=random.choice(lst_ip))  # 发送请求
    resp.encoding = 'gbk'  # 处理编码
    print(resp)
    html = etree.HTML(resp.text)  # 用etree 封装网页
    download_url = html.xpath('//*[@id="djxz"]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a/@href')  # 通过xpath定位下载链接
    name = html.xpath('/html/body/div[5]/div/div[1]/div/div[1]/text()')  # 通过xpath找到小说名字

    # 保存文件
    with open(f'{name[0]}.rar', 'wb') as w:
        w.write(requests.get('http://www.12z.cn' + download_url[0], headers=headers).content)  # 下载文件
        print(f'成功下载文件{name[0]}')


def executor():
    url = 'http://www.12z.cn/book/wuxiaxianxia/list_13_1.html'
    # 发送GET请求获取页面内容，从代理池中使用随机ip
    resp = requests.get(url, headers=headers, proxies=random.choice(lst_ip))
    resp.encoding = 'gbk'
    # 使用lxml解析页面内容
    html = etree.HTML(resp.text)
    # XPath所有的小说的链接/html/body/div[5]/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[2]/div[1]/a
    divs = html.xpath('/html/body/div[5]/div[2]/div[3]/div/div[1]/div')
    # print(urls)
    # 遍历所有的单元div
    lst_div = []
    for div in divs:
        # 找到进入小说详情页的href
        href = div.xpath('./div[1]/div[2]/div[1]/a/@href')
        lst_div.append(href)
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in lst_div:
            t.submit(simple_down, url=i[0])

        t.shutdown()


# 模拟异步协程的爬虫操作
async def download_test(url):
    print("开始下载", url)
    await asyncio.sleep(3)  # 模拟爬虫中遇到的同步操作，如请求等
    print("结束下载", url)


# 为了避免在主函数中有太多的代码行数，我们手动创建一个主函数
async def main():
    urls = [1, 2, 3, 4, ]  # 模拟url
    task = []  # 创建任务列表
    for url in urls:
        # 使用asyncio.cteate_task() 命令把函数包装，添加到任务列表中
        task.append(asyncio.create_task(download_test(url)))
    await asyncio.wait(task)  # 执行任务列表中的操作


if __name__ == '__main__':
    asyncio.run(main())  # 执行手动创建的主函数
