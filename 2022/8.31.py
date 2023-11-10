# 导入模块
import asyncio
import time

# 定义函数


async def func1():
    print('就让这枫叶都染成红色吧')
    await asyncio.sleep(4)
    print('鬼女红叶')


async def func2():
    print('本大爷的名号无人不晓')
    await asyncio.sleep(3)
    print('酒吐童子')


async def func3():
    print('小鱼干！！喵喵喵')
    await asyncio.sleep(4)
    print('九命猫')


async def main():  # 再定义一个函数，将需要异步的函数放进一个列表里
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)  # 将列表内容异步协程化

time1 = time.time()  # 计时开始
if __name__ == '__main__':
    asyncio.run(main())
time2 = time.time()  # 计时结束
print(time2-time1)
