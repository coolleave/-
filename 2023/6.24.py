# 导入多线程
from threading import Thread

# 定义循环函数
# def func():
#     for i in range(1, 1000):
#         print(i, 'son')

# 主程序运行
# if __name__ == '__main__':
#     t = Thread(target=func)  # 用线程池运行已定义函数
#     t.start()
#     for a in range(1000, 2000):
#         print(a, 'main')
# 导入线程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 定义函数
# def func1(c):
#     for b in range(1, 5000):
#         print(b, c)
#
#
# func1('hh')
#  用50个线程跑程序
# with ThreadPoolExecutor(50) as t:
#         t.submit(func1, c=f'线程')

import requests
url = 'https://gk.hebeea.edu.cn/hebgk/'
resp = requests.get(url)
print(resp)
