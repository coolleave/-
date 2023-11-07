"""
解决汉诺塔问题的步骤
问题：
分别有n个铁饼在a杆子上，有bc两个空杆子，求将所有的铁饼移动到c杆子上
1、首先将n-1个铁饼从a经过c到b杆子
2、将最后一个铁饼移动到c杆子上
3、将b柱子所有的铁饼经过a到c上

闭包
闭包的本质就是外部对局部变量的调用
闭包的优点
1、安全性，外部不能够修改局部变量
2、可以让局部变量常驻内存

装饰器 是在不改变原来函数的基础上，给函数添加新的功能
"""


def hanoi(n, a, b, c):  # 汉诺塔问题
    if n > 0:
        hanoi(n-1, a, c, b)
        print(f'{a}移动到{c}')
        hanoi(n-1, b, a, c)


def func():  # 闭包
    a = 10

    def func1():
        print(a)
        return a
    return func1


def first_wrapper(fn):  # 装饰器
    def inner():
        print('装饰前面')
        fn()
        print('装饰后边的内容')
    return inner


def add():  # 装饰器测试用函数
    print('我是新增函数')


# 通用装饰器的写法
def wrapper(fn):  # 装饰器外壳函数
    def inner(*args, **kwargs):  # 装饰器内层函数
        """ 执行函数之前的操作"""  # 装饰行为
        ret = fn(*args, **kwargs)  # 被装饰的函数，并且使用ret接收返回值
        """ 执行函数之后的操作"""
        return ret  # 返回返回值
    return inner  # 返回内层函数，


@wrapper  # 使用@ 来调用装饰器，直接装饰函数
def target():
    pass


if __name__ == '__main__':
    # hanoi(1, 'A', 'B', 'C')
    target()
    