import sys
import time
import os


def sys1():
    print(sys.getsizeof(66))  # 查看占了几个字节


def time1():
    print(time.localtime(time.time()))


def os1():
    # os.system('D:\\WeChat\\WeChat.exe')  # 转义字符需要加一个\，变成两个\\
    path = os.getcwd()
    print(type(path))
    lst = os.listdir(path)
    for i in lst:
        if i.endswith('.py'):
            print(i)


if __name__ == '__main__':
    os1()
