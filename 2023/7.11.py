# 第一个练习
def ret():
    global lst
    lst = [88, 89, 90, 91, 00]
    print(lst)
    # 以上是员工的残缺出生日期，把他恢复成原样
    lst_1 = []
    for num in range(len(lst)):
        i = lst[num]
        if i == 0:
            i = '200' + str(i)
            lst_1.append(i)
        else:
            i = '19' + str(i)
            lst_1.append(i)
    print(lst_1)


# 再来一种方法
def ret1():
    print(lst)
    lst_1 = []
    for index, value in enumerate(lst):
        if value == 0:
            lst_1.append('200' + str(value))
        else:
            lst_1.append('19' + str(value))
    print(lst_1)
    print()


# 小技巧，利用bool判断奇数，偶数
def bool_():
    odd = []
    even = []
    for i in range(11):
        # 用i除以2 取余数，如果余数为零，则bool值为False，如果不为零为True，就在奇数列表中追加
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    print(f'奇数有{odd}偶数有{even}')


# 利用递归函数解决阶乘问题
def jc(n):
    n = int(n)
    if n == 1:
        return 1
    else:
        return n * jc(n-1)


# 利用递归函数解决斐波那契函数
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(100))