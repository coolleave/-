def trouble():
    h = int(input())  # 接收行数
    dic = {}
    for i in range(h):  # 接收数据与存储
        s = input().split()
        dic[i + 1] = s


def findmax(n,lst):
    lst1 = []  # 准备列表
    sum = 0  # 接收和
    for a in range(1, n+1):  # 遍历列表行
        if a == 1:
            sum += lst[n+1][0]  # 递归
            findmax(n-1, lst)
        if a == n:
            sum += lst[n+1][-1]
            findmax(n, lst)
        else:
            sum += lst[n+1][n]


def triple():
    for i in range(100000000000000000000):
        if i % 3 == 0:
            print(i)


if __name__ == '__main__':
    triple()

