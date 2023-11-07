"""

eval() 将字符串内容执行为代码，有返回值
进制转化
bin() 将数字转化为二进制
oct() 将数字转化为八进制
hex() 将数字转化为十六进制  0-f  10--->a
数学相关
abs() 求绝对值
divmod()  除法  (商，余数)
round()  四舍五入
pow()  乘方
sum()  求和
max() 求最大值    min() 求最小值
frozenset 不可变的集合
list  不可变的列表就是元组

any判断bool值相当于or
all判断bool值相当于and

zip拉链函数 可以快速将两个列表构建一个字典

reverse 把列表翻转返回一个迭代器
slice 是切片

字符相关
ord  将字符转化为对应的在编码中的数字
chr  将对应数字转化为字符

repr 一个字符串最应该显示的效果
r字符串 不想用转译字符，在正则中会用到还原转义字符的字符串作用
format 格式化字符串，有三个作用
1、定长整数
2、保留小数
3、二进制

sorted 排序 reverse是否倒序 默认从小到大
sorted 也可以自定义规则
filter  把所需要的对象摘出来，筛选函数
map     把可迭代的对象依次统一做相同的操作，叫做映射函数

递归就是自己调用自己

"""
import random
import os


def asck():  # 打印所有数字对应文字
    for i in range(1, 65536):
        print(chr(i), end='')


def yzm():  # 生成四位随机英文大小写验证码
    i = 0
    while i < 4:
        n = random.randint(65, 123)
        if n <= 90 or n >= 97:
            print(chr(n), end='')
            i += 1


def gsh():  # 格式化
    print(format(48, '08d'))  # 将数字定长为8位数字，前边补零，d为整数 0为填充物，8是长度
    print(format(32, '08b'))  # b表示二进制，08表示位数
    print(format(1.23, '.9f'))  # f表示保留小数 .9表示保留九位数字
    print(format(223232323, 'e'))  # 科学计数法


def sort():  # 排序
    global lst
    lst = [1, 3, 556, 77, 88]
    print(sorted(lst))


def sx():  # 筛选函数
    global lst
    lst = [1, 3, 4, 5, 6, 7, 88, 74]
    s = filter(lambda x: x % 2 == 0, lst)  # 从这里可以看出匿名函数的作用，只需要一行代码就可以。
    for i in s:                            # 而且匿名函数和excel中的函数有异曲同工之妙
        print(i)


def ys():  # 映射函数
    global lst
    lst = [1, 4, 5, 6, 7, 8, 3, 2, 5]
    s = map(lambda x: x + 1, lst)
    print(list(s))


def dg(path, ceng):  # 利用递归来遍历文件夹所有的文件
    global lst
    lst = os.listdir(path)  # 找到当前路径下所有的路径
    # print(lst)
    for name in lst:  # 遍历所有文件路径
        real_path = os.path.join(path, name)  # 将文件路径拼接成完整的文件路径
        if os.path.isdir(real_path):  # 判断为文件夹
            print('\t'*ceng, name)  # 分层显示
            dg(real_path, ceng+1)  # 进入该文件夹，继续执行函数完成递归
        else:  # 为普通文件
            print('\t'*ceng, name)


lst = [1, 2, 4, 6, 7, 8, 9, 9, 0, 6, 4, 55, 6, 33, 3, 7, 88888, 4, 445, 4324, 54, 4535, 2343, 5, 55232]
a = int(input('>>>>'))


def com():  # 利用二分法查看数字是否在列表当中
    lst.sort()
    print(lst)
    left = 0
    right = len(lst) - 1
    while right >= left:
        mid = (left + right) // 2
        if lst[mid] > a:
            right = mid - 1
        if lst[mid] < a:
            left = mid + 1
        if lst[mid] == a:
            print('找到了，位置', mid)
            break
    else:
        print('没找到')


if __name__ == '__main__':
    com()
