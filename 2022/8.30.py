import asyncio
import time


async def func1():
    print('我是金克丝')
    # time.sleep(4)  # 当程序出现同步操作时，异步协程就停止了
    await asyncio.sleep(4)  # 异步操作的代码

    print('我是金克丝')


async def func2():
    print('我是厄斐琉斯')
    # time.sleep(4)
    await asyncio.sleep(4)
    print('我是厄斐琉斯')


async def func3():
    print('我是王大拿')
    # time.sleep(5)
    await asyncio.sleep(5)
    print('我是王大拿')

if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()

    tasks = [
        f1,
        f2,
        f3
    ]
    # 一次性启动多个任务协程
    time1 = time.time()
    asyncio.run(asyncio.wait(tasks))
    time2 = time.time()
    print(time2-time1)

