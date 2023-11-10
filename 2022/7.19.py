# a = 250
# print(bool(a))
# print(float(a))
# print(complex(a))
#
# print(bin(a))# 二进制转换
# print(oct(a))  # 八进制转换
# print(hex(a))  # 十六进制转换
# print(pow(8, 9))  # 次幂
# lst = [34, 4, 5, 5, 6]
# print(sum(lst))  # 求和
# print(max(lst))  # 最大值
# print(min(lst))  # 最小值

# a = 34
# print(format(a, "b"))  # b表示二进制 o表示八进制 x表示十六进制
# print(format(a, "08b"))  # 表示填充至8个字符表示 只填充不切割

# b = "陈"
# print(ord(b))  # ord 表示在Unicode中的码位
# b = "鹏"
# print(ord(b))
# b = "宇"
#

for i in range(65536):
    print(chr(i) + " ", end="")
