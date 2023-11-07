# 导入协程包
import asyncio
import time


# # 创建一个协程对象，此时这个函数是简单的函数
# async def func():
#     print('我是异步协程')
#
# if __name__ == '__main__':
#     asyncio.run(func())  # 使用特定的步骤来执行异步对象


# 先来看看同步操作
# def func1():
#     print('我睡了3秒')
#     time.sleep(3)
#
#
# def func2():
#     print('我睡了1秒')
#     time.sleep(1)
#
#
# def func3():
#     print('我睡了2秒')
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#
#     t1 = time.time()
#     func1()
#     func2()
#     func3()
# #     t2 = time.time()
#     print(f'我共睡了{t2-t1}秒')


# 以上代码输出结果为 我共睡了6.029406785964966秒
# 接下来我们来看看异步协程的效率

# 首先创建异步协程对象函数

async def func1():
    print('我一共睡了3秒')
    await asyncio.sleep(3)  # 用asyncio来使用睡眠，同时使用await来修饰，这样才能达到异步协程的目的


async def func2():
    print('我一共睡了1秒')
    await asyncio.sleep(1)


async def func3():
    print('我一共睡了2秒')
    await asyncio.sleep(2)

# tasks = [func1(), func2(), func3()]
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks))  # 这个是使用异步协程来执行所选定函数列表
#     t2 = time.time()
#     print(f'我睡了{t2-t1}秒')


# 主程序的输出结果为：我睡了3.0163538455963135秒，可见异步协程效率很高

# 下面我们使用推荐写法

# 首先定义一个main函数
async def main():
    tasks = [
        asyncio.create_task(func1()),  # 将函数封装成一个异步对象
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
        ]
    await asyncio.wait(tasks)  # 将任务列表装饰成异步对象


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())  # 用异步协程来执行函数
    t2 = time.time()
    print(f'我睡了{t2-t1}秒')
# 程序完美运行
