"""
今天干91看剧
方法步骤
1、拿到网页源代码用正则解析出m3u8网址
2、读取m3u8文件，拿到视频下载链接
3、通过链接下载视频
4、合并视频
思路说完了 接下来就正式开始啦
"""
# 导入模块
import requests
import re
import asyncio
import aiohttp
import aiofiles


def m3u8_get():
    # 解析网址
    url = 'http://www.91kanju2.com/vod-play/62844-2-1.html'
    resp = requests.get(url)
    # print(resp.text)
    # 写正则
    obj = re.compile(r"url: '(?P<url>.*?)'", re.S)
    m3u8 = obj.findall(resp.text)[0]
    # print(url)
    resp.close()
    m3u8_open(m3u8)


# 下载
def m3u8_open(url):
    resp = requests.get(url)
    with open('柯曼先生.m3u8', mode='w', encoding='utf-8')as f:
        f.write(resp.text)
    resp.close()
    print('m3u8下载完成')


# 解析m3u8文件
async def dw_m3u8():
    n = 1
    with open('柯曼先生.m3u8', mode='r', encoding='utf-8')as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            else:
                async with aiohttp.ClientSession().get(line) as resp:
                    async with aiofiles.open(f'../程序/柯曼先生/{n}.ts', mode='wb')as w:
                        await w.write(resp.content)
                        n = n+1
                resp.close()


if __name__ == '__main__':
     m3u8_get()
