import requests
import asyncio
import aiohttp
import aiofiles
from lxml import etree
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
import re
import time
# 准备请求头
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
           'Referer': 'https://pvp.qq.com/'}
# 创建无头浏览器
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# 定义进入王者网站的函数


async def main():
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    web = Edge(options=opt)
    web.get(url)
    li_list = web.find_elements('xpath', '/html/body/div[3]/div/div/div[2]/div[2]/ul/li')
    tasks = []
    for li in li_list:
        tasks.append(get_url(li))
        await asyncio.wait(tasks)


async def get_url(li):
    tasks = []
    name = li.find_element('xpath', './a').text  # 获取文本
    href = li.find_element('xpath', './a').get_attribute('href')  # 获取标签属性
    print(name)
    print(href)
    resp = requests.get(href)
    resp.encoding = 'gbk'
    # tree = etree.HTML(resp.text)
    # print(resp.text)
    obj = re.compile(r"background:url(?P<url>.*?)center", re.S)
    kid_url = obj.findall(resp.text)
    # print(kid_url[0])
    url = 'https:' + kid_url[0].split("'")[1]
    # print(url)
    tasks.append(asyncio.create_task(aio_download(url, name)))
    await asyncio.wait(tasks)


async def aio_download(url, name):
    async with aiohttp.ClientSession() as s:
        async with s.get(url, headers=headers) as resp:
            # print(resp.text)
            async with aiofiles.open(f'图片/{name}.jpg', mode='wb') as f:
                await f.write(await resp.content.read())


if __name__ == '__main__':
    time1 = time.time()
    asyncio.run(main())
    time2 = time.time()
    print(time2-time1)
