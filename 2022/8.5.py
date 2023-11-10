# # 正则模块
# import re
# lst = re.findall(r"\d+", '我的电话号是:15233443094')
# print(lst)  # findall匹配字符串里所有符合条件的字符串
# 迭代器补课
# for c in 234:
#     print(c)  # 程序报错 原因是整型不可迭代
# a = iter('我叫旁叶易寒')
# b = 0
# for b in range(len('我叫旁叶易寒')):
#     print(next(a))
# a = 'hh'.__iter__()
# print(a)

# # python 小练习 两数之和
# number1 = float(input('请输入数字'))
# number2 = float(input('请输入数字'))
# su = number1 + number2
# print(f'{number1}+{number2}={su}')

# 数字的阶乘
n = int(input('请输入正整数'))
val = 1


def jc():
    global val
    global n
    if n < 0:
        print('请输入正整数')
    if n >= 0:
        while n >= 1:
            val = val*n
            n = n-1
    return val


m = int(input('请输入正整数'))
val1 = 1


def jc1():
    global val1
    global m
    global n
    c = n - m
    while c >= 1:
        val1 = val1*c
        c = c-1
    return val1


print(jc())
print(jc1())

print(int(jc()/jc1()))
