# 导入模块
import requests
import asyncio
import aiohttp
import aiofiles
"""
操作过程扒光一部小说
1、同步操作 请求getCatalog 得到拿到所有的章节cid的名称
2、异步操作 请求getChapterContent 得到小说内容
"""

"""
https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}
https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|1569782244%22,%22need_bookinfo%22:1}
"""
b_id = '224306063500'
u = 'https://dushu.baidu.com/api/pc/getCatalog?' \
          'data={%22book_id%22:%' + b_id + '%22}'


async def aio_download(bid, cid, name):
    # 拿到url
    url = 'https://dushu.baidu.com/api/pc/getChapterContent?' \
          'data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|' + f'{cid}' + '%22,%22need_bookinfo%22:1}'
    # 准备异步

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()  # 将请求以json写入
            async with aiofiles.open(f'../程序/西游记/{name}.txt', mode='w', encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])  # 把小说的内容写入文件
            # print(dic['data']['novel']['content'])


async def log(url):
    resp = requests.get(url)
    # print(resp.text)
    dic = resp.json()  # 以json创建一个字典
    items = dic['data']['novel']['items']  # 拿到所有的章节
    # print(items)
    tasks = []
    for item in items:
        name = item['title']
        c_id = item['cid']
        # print(name, c_id
        task = asyncio.create_task(aio_download(b_id, c_id, name))
        tasks.append(task)

    await asyncio.wait(tasks)


if __name__ == '__main__':

    asyncio.run(log(u))



