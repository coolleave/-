import requests
import re
import asyncio
import aiofiles
import aiohttp

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'}


# 定义函数，获取第一个m3u8文件
def f_m3u8_url(m3u8_url):
    resp = requests.get(m3u8_url, headers=headers)  # 请求m3u8网址
    # print(resp.text)
    # 利用re获取first m3u8文件
    obj = re.compile(',"url":"(?P<f_m3u8>.*?)","next":"","name', re.S)  # 定义所需正则表达式
    f_url = obj.finditer(resp.text)  # 利用正则提取第一个m3u8的网址
    print('提取first url 完毕')
    for i in f_url:
        f_url = i.group('f_m3u8')
        f_url = f_url.replace("\\", '')  # 去除冗余的"\"符号
        print(f_url)
    resp1 = requests.get(f_url, headers=headers)  # 请求到网址
    with open('大话西游/1m3u8.m3u8', mode='wb') as f:  # 写入first m3u8 文件
        f.write(resp1.content)
    print('写入first_url 完毕')
    domain = f_url.split('20220329')[0]  # 得到主域名
    # print(domain)
    hand_s_url(domain)  # 调用下一个函数


# 得到并处理第二个url，下载second m3u8文件
'''
https://vod2.bdzybf7.com/20220329/nBeH3PR9/2000kb/hls/index.m3u8?_=1685018910934
'''


def hand_s_url(domain):
    with open('大话西游/1m3u8.m3u8', mode='r') as f:  # 阅读first m3u8文件，提取其中的url
        for i in f:  # 筛选符合条件的行
            if i.startswith('#'):
                continue
            else:
                s_url = domain + i
                print(s_url)
    resp = requests.get(s_url, headers={'User-Agent':
                                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                        '(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'})
    # 请求second url
    with open('大话西游/2m3u8.m3u8', mode='wb') as f:  # 保存第二个m3u8文件
        f.write(resp.content)


# 使用异步协程爬取ts片段
async def aio_download(download_url, name):
    async with aiohttp.ClientSession() as s:
        async with s.get(download_url, headers=headers) as r:
            async with aiofiles.open(f'大话西游/ts/{name}.ts', mode='wb') as f:
                await f.write(r.content.read())
                print(f'{name}完成')


#  定义异步主函数
async def main():
    async with aiofiles.open('大话西游/2m3u8.m3u8', mode='r') as f:  # 异步文件打开过滤无用行
        a = 1
        tasks = []
        async for i in f:
            if i.startswith('#'):
                continue
            else:
                tasks.append(asyncio.create_task(aio_download(i, a)))  # 创建异步任务
                a += 1
        await asyncio.wait(tasks)  # 包装异步任务

if __name__ == '__main__':
    url = 'http://www.fuqiangjiazheng.com/xijupian/dahuaxiyouzhiyueguangbaohe/1-1.html'
    f_m3u8_url(url)
    asyncio.run(main())  # 执行异步任务
