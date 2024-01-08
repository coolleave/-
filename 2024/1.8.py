a = m = 15
b = n = 20
# 辗转相除求出最大公约数和最小公倍数
while a % b != 0:
    a, b = b, a % b
print(b, m*n//b)


# print("商为", 15//20, "余数为", 15 % 20)