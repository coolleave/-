import aiofiles
import aiohttp
import asyncio
import requests
import os


# 定义单个章节下载函数
async def download_chapters(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()  # 拿到有题目和内容的字典
            title = dic['data']['novel']['chapter_title']
            async with aiofiles.open(f'红楼梦/{title}.txt', mode='w') as f:
                await f.write(dic['data']['novel']['content'])
                print(f'{title} over!')


async def get_url():
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306340004%22}'
    resp = requests.get(url)
    dic = resp.json()
    items = dic['data']['novel']['items']  # 找到title和cid的位置
    tasks = []  # 创建异步任务列表

    for item in items:  # 找出每个title和cid

        cid = item['cid']
        # print(title, cid)
        # 搞出每个章节的url
        url = 'https://dushu.baidu.com/api/pc/getChapterContent?data={' + \
              f'%22book_id%22:%224306340004%22,%22cid%22:%224306340004|{cid}%22,%22need_bookinfo%22:1' + '}'
        tasks.append(asyncio.create_task(download_chapters(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # os.mkdir('红楼梦')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_url())

