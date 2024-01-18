import aiohttp
import asyncio
import threading


# 定义函数
def func():
    for a in range(1000):
        print(a, '线程')


if __name__ == '__main__':
    t = threading.Thread(target=func)  # 创建线程
    t.start()  # 线程可以执行了，具体时间由cpu决定
    for i in range(1000):
        print(i, '主线程')
