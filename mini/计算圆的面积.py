import math
r = float(input('请输入半径'))


def area():
    global r
    s = round(math.pi*r*r, 2)
    return s


s = area()
print(s)

