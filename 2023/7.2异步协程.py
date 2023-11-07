import aiohttp
import asyncio
# 准备所需要下载的链接
urls = [

]


# 定义异步函数
async def ai_download(url):
    # 使用异步协程版requests来请求网址
    async with aiohttp.ClientSession() as session:  # 必须使用上下文管理器
        async with session.get(url) as resp:  # 必须使用async上下文管理器来得到请求
            name = url.split('/')[-1]  # 切割到名字
            with open(f'{name}', mode='wb') as f:  # 使用上下文管理器创建文件
                f.write(await resp.content.read())


# 定义执行主函数
async def main():
    tasks = []  # 创建协程任务列表
    for url in urls:
        tasks.append(asyncio.create_task(ai_download(url)))  # 将协程任务包装，扔进列表
    await asyncio.wait(tasks)  # 要在前面加上await

if __name__ == '__main__':
    asyncio.run(main())  # 在主程序中运行主函数

