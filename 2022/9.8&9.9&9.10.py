"""
今天爬取视频 看着非常地复杂 加油
首先 基本不步骤分为6步
1、拿到网页源码，找到 iframe
2、拿到iframe的第一层m3u8文件的url、
3、通过第一层m3U8文件的url拿到第二层m3u8的url（视频存放路径）
4、下载视频
5、拿到秘钥，解密
6、合并视频
"""
# 导入模块
import requests
import re
import aiohttp
import aiofiles
import asyncio
import time
import os


# 拿到第一层网址
def first_url(url1):
    resp = requests.get(url1)
    # print(resp.text)
    obj = re.compile(r'{url: "(?P<url1th>.*?)"')
    url1th = obj.finditer(resp.text)
    print('网址请求完成！')
    for i in url1th:    # print(i.group('url1th'))
        url_1 = i.group('url1th')
        print('正则匹配完成!')
        return requests.get(url_1)


def save_m3u8(resp):  # 保存m3u8文件
    with open('../抓视频/1th.m3u8', mode='wb') as f:
        f.write(resp.content)
        print('m3u8文件已经保存！')
    # https://cache.changjiebaihuo.cn/Ym5jFlUZ-awm54QyWQg8KHSc9y9KURfahJnnij2WfiZRt2wSyvVCh5U2u6tIV3PjHXbZtUPphELgrTFYVQ3DKw/004.ts


# 下载m3u8里的ts文件
async def download_ts(d_url, n, session):
    async with session.get(d_url) as resp:
        async with aiofiles.open(f'../抓视频/{n}.ts', mode='wb')as w:
            await w.write(await resp.content.read())
            print(f'{n}下载完成')
    resp.close()


async def aio_download(url3):
    async with aiofiles.open('../抓视频/1th.m3u8', mode='r')as f:
        print('m3u8文件读取完成！')
        tasks = []
        n = 1
        async with aiohttp.ClientSession()as session:
            async for line in f:
                if line.startswith('#'):
                    continue
                else:
                    line.strip()
                    n += 1
                    d_url = url3+line
                    # print(d_url, '\n')
                    task = asyncio.create_task(download_ts(d_url, n, session))
                    tasks.append(task)
            await asyncio.wait(tasks)
            f.close()
# https://qq1977134614.rx9696mv.com:8866/Ym5jFlUZ-awm54QyWQg8KHSc9y9KURfahJnnij2WfiZBh4sLr2TfMZ8NAWLoa_yoJLoq-KrOBxqqMeDaT9QdzQ/004.ts


# 视频合并
def merge_ts():
    s = []
    for i in range(2, 500):
        i = str(i)
        lj = f"../抓视频/{i}.ts"
        s.append(lj)
    v_str = "+".join(s)
    print(v_str)
    os.system(f"copy /b {v_str} > ../抓视频/视频.ts")


if __name__ == '__main__':
    url = 'https://www.jsyb.cc/tgplayer/?url=TuGou-My12XzE0b2ppdXdvMzJj'
    # ret = first_url(url)

    # save_m3u8(ret)  # 下载m3u8的文件
    # 这个网站和我们想像中的不太一样 这个没有第二个m3u8文件 所以 我们直接进入下载视频阶段
    # noinspection SpellCheckingInspection
    video_url = 'https://qq1977134614.rx9696mv.com:8866/' \
                'bwBnjqM9aZzV8csShVrfPo0b835akea_Dg11TY2zPC9fT2Iav2_UZuJ-KA36WTgU7erK_QFd5RlWA-Z4y3_-Pw/'
    time1 = time.time()
    # asyncio.run(aio_download(video_url))

    # noinspection SpellCheckingInspection
    m3u8_url = 'https://qq1977134614.rx9696mv.com:8866/bwBnjqM9aZzV8csShVrfPo0b835akea_' \
               'Dg11TY2zPC87h5PlsqLb6gYTXTXLUVMYszH5Jh0jzacYHVFaRnRQYw/RongXingVR'
    time2 = time.time()
    print(time2 - time1)
    # 合并视频！
    merge_ts()
    # 搞定！
