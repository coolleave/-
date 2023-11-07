"""
题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了
�
N 个 1 到 1000 之间的随机整数（
�
≤
100
N≤100），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作。

输入描述
第 1 行为 1 个正整数，表示所生成的随机数的个数：
�
N。

第 2 行有
�
N 个用空格隔开的正整数，为所产生的随机数。

输出描述
输出 2 行，第 1 行为 1 个正整数
�
M，表示不相同的随机数的个数。

第 2 行为
�
M 个用空格隔开的正整数，为从小到大排好序的不相同的随机数。

输入输出样例
示例 1
输入

10
20 40 32 67 40 20 89 300 400 15
copy
输出

8
15 20 32 40 67 89 300 400
"""


def sort():
    a = int(input())
    b = list(set(input().split(" ")))
    b_new = []
    for i in b:
        b_new.append(int(i))
    b_new.sort()

    print(len(b_new))
    for d in b_new:
        print(d, end=" ")

    # print(len(c))
    # print(c)


def momo():
    n, k, m = map(int, input().split())  # 输入数据
    a = list(range(1, n + 1))  # 准备列表
    i = k - 1  # 初始位置
    while len(a) > 0:
        i = (i + m - 1) % len(a)  # 初始位置为i 往后了m - 1个索引，所以是 i + m -1
        print(a.pop(i))  # 删除当前索引的元素



def ff():
    n, k, m = map(int, input().split())  # 输入参数
    i = k - 1
    a = list(range(1, n +  1))
    while len(a) > 0:
        i = (i + m - 1) % len(a)
        print(a.pop(i))


def test():
    n, k, m = map(int, input().split(" "))  # 输入数据
    print(n, k, m)
    n, k, m = map(int, input().split())  # 输入数据
    print(n, k,m)



if __name__ == '__main__':
    test()
