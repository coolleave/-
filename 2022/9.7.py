# 今日测试异步协
import aiofiles
import asyncio
import time


def write():
    n = 0
    for n in range(1000):
        with open(f'../程序/测试/n{n}.txt', mode='w',encoding='utf-8')as f:
            f.write(str(n))
            n += 1


async def write1():
    a = 0
    for a in range(1000):
        async with aiofiles.open(f'../程序/测试/a{a}.txt', mode='w', encoding='utf-8')as f:
            await f.write(str(a))
# if __name__ == '__main__':
#     time1 = time.time()
#     asyncio.run(write1())
#     time2 = time.time()
#     print(time2-time1)
#
#     time3 = time.time()
#     write()
#     time4 = time.time()
#     print(time4 - time3)

