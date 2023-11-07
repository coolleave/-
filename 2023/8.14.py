"""
    你设计的矩形页面必须等于给定的目标面积。
宽度 W 不应大于长度 L ，换言之，要求 L >= W 。
长度 L 和宽度 W 之间的差距应当尽可能小。
返回一个 数组 [L, W]，其中 L 和 W 是你按照顺序设计的网页的长度和宽度。
"""


def constructRectangle():  # 构造矩形
    area = 122122
    lst = []
    for w in range(1, area + 1):  # 暴力遍历面积内所有整数
        if not area % w:  # 找到能整除的
            l = area // w  # 再挑选出小于l的
            if l >= w:
                lst.append((l, w))  # 将所有l和w添加到列表中
    return lst[-1]  # 因为w是从大到小的，所以满足条件的w的最大值就是所求，就是列表最后一个。


def constructRectangle1():  # 方法2，大佬的方法，积的二分法
    import math
    area = 122122
    w = int(math.sqrt(area))  # 将面积开方并且取整二分法，
    while area % w:  # 找到可以被面积整除的，再利用二分法，直接选取满足条件的最大整数宽
        w -= 1
    return area // w, w


'''
本题收获，
求一个数是否能整除用 a % b 的布尔值判断
a % b 为求 a 除以 b的余数
如果能整除，则a % b的值为0 也就是布尔值为false
如果不能整除，则a % b的值不为零，则布尔值为 true

'''

if __name__ == '__main__':
    print(constructRectangle1())
