# 今日打卡
# 判断一段字符串中 是否含有相同的单个字符
# 思路就是 把字符串转化为集合去重，然后判断集合的长度
def pro1():
    s = input("这是一段字符")
    if len(set(s)) == len(s):
        print("YES")
    else:
        print("NO")


def pro2():  # 小王子单链表
    m = int(input())  # 排序次数
    lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for i in range(m):
        x = input()
        lst.remove(x)
        lst.insert(0, x)
        a = " ".join(lst)
        print(a)


if __name__ == '__main__':
    pro2()

