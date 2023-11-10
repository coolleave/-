# 自主写程序干西游记

# 导入模块
import requests
import asyncio
import aiohttp
import aiofiles

# 准备链接
url1 = 'https://dushu.baidu.com/api/pc/getCatalog?' \
       'data={%22book_id%22:%224306063500%22}'
b_id = '224306063500'
url2 = 'https://dushu.baidu.com/api/pc/getChapterContent?data=' \
       '{%22book_id%22:%224306063500%22,%22cid%22:%224306063500|1569782244%22,%22need_bookinfo%22:1}'


async def content(cid, name):
    url = 'https://dushu.baidu.com/api/pc/getChapterContent?' \
          'data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500' \
          '|' + f'{cid}' + '%22,%22need_bookinfo%22:1}'  # 将url拿到 整理好
    async with aiohttp.ClientSession().get(url) as resp:  # 用异步进行请求
        dic = await resp.json()  # 将请求用json的格式储存
        async with aiofiles.open(f'../程序/西游记/{name}.txt', mode='w', encoding='utf-8') as f:
            await f.write(dic['data']['novel']['content'])


async def get_id():
    resp = requests.get(url1)
    # print(resp.text)
    dic = resp.json()
    items = dic['data']['novel']['items']
    # print(type(dic))
    # print(type(items))
    tasks = []
    for i in items:
        name = i['title']
        cid = i['cid']
        # print(name, cid)
        task = asyncio.create_task(content(cid, name))
        tasks.append(task)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(get_id())
