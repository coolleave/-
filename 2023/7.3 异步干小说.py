# 导入包
import requests
import aiohttp
import asyncio
import aiofiles
# 先把函数定义完，找到大纲思路
"""
url = https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306340004%22}
"""


# 定义异步协程下载函数
async def aio_download(title, url):  # 准备好相应的参数
    async with aiohttp.ClientSession() as session:  # 创建异步版网络请求
        async with session.get(url) as resp:  # 使用异步版网络请求
            dic = await resp.json()  # 将请求格式化为json的格式，一定要带着await，async后一定要接着await！！！
            async with aiofiles.open(f'./红楼梦/{title}', mode='w') as f:  # 使用异步文件保存
                await f.write(dic['data']['novel']['content'])  # 异步保存文件内容
                print(f'{title} over!')


# 定义主函数
async def main():
    # 访问本书的domain
    resp = requests.get('https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306340004%22}')
    dic = resp.json()  # 将请求格式化为json格式
    items = dic['data']['novel']['items']  # 找到title和cid的位置
    tasks = []  # 创建异步任务列表

    for item in items:  # 找出每个title和cid
        title = item['title']
        cid = item['cid']
        # print(title, cid)
        # 搞出每个章节的url
        url = 'https://dushu.baidu.com/api/pc/getChapterContent?data={' + \
              f'%22book_id%22:%224306340004%22,%22cid%22:%224306340004|{cid}%22,%22need_bookinfo%22:1' + '}'
        tasks.append(asyncio.create_task(aio_download(title, url)))  # 将每个异步任务放进列表里
    await asyncio.wait(tasks)  # 执行异步任务
if __name__ == '__main__':
    asyncio.run(main())

# 程序完美执行，over！！

