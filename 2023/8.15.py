"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

    字符          数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
    同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
    给定一个罗马数字，将其转换成整数。
"""


def romanToInt():
    s = 'MCMXCIV'
    sum = 0
    if 'IV' in s:
        sum += 4
        s = s.replace('IV', '')
    if 'IX' in s:
        sum += 9
        s = s.replace('IX', '')
    if 'XL' in s:
        sum += 40
        s = s.replace('XL', '')
    if 'XC' in s:
        sum += 90
        s = s.replace('XC', '')
    if 'CD' in s:
        sum += 400
        s = s.replace('CD', '')
    if 'CM' in s:
        sum += 900
        s = s.replace('CM', '')
    for i in s:
        if i == 'M':
            sum += 1000
        elif i == 'D':
            sum += 500
        elif i == 'C':
            sum += 100
        elif i == 'L':
            sum += 50
        elif i == 'X':
            sum += 10
        elif i == 'V':
            sum += 5
        elif i == 'I':
            sum += 1
    return sum


"""
定解消元法，在本题中存在六种特殊情况，这样的话我们就可以将这六种定解列出来，将定解添加到sum中
并且，将s中的字符串给消除掉，再使用键值对比对，遍历字符串，加上对应值。
"""


if __name__ == '__main__':
    print(romanToInt())
