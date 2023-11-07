def s():
    r1 = float(input())
    r2 = float(input())
    h = float(input())
    v = 1/3 * 3.14 * h * (r1*r1 + r2*r2 + r1*r2)
    print('%.3f' % v)


def money():
    mon = int(input("请输入钱数"))
    mon100 = 0
    mon20 = 0
    mon10 = 0
    mon1 = 0
    while mon > 0:
        if mon >= 100:
            mon -= 100
            mon100 += 1
            continue
        elif 100 > mon >= 20:
            mon -= 20
            mon20 += 1
        elif 20 > mon >= 10:
            mon -= 10
            mon += 1
        elif 10 > mon >= 1:
            mon -= 1
            mon1 += 1
    print(f"100元的需要{mon100}张，20元的需要{mon20}张，10元的需要{mon10}张，1元的需要{mon1}张")


def fun1():
    a = 1
    while a == 1:
        pass


if __name__ == '__main__':
    money()
