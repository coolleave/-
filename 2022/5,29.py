# a = "我叫旁叶易寒你叫什么"
# print(a[:])  # 前后不加东西可以直接从头到尾地输出字符串里的元素
# print(a[5])  # 这是第六个书因为从零开始数
#
# print(a[0])  # 0表示第一个数 一次类推
# print(a[-1])  # 负数表示倒数
# print(a[2:6])  # 区间左开右闭 一共有四个元素
# print(a[-3:-1]) #导数依然成立
# print(a[-1:-3])  # 这样就不行了 因为区间是从左往右数的 不能违背从左往右的原则
# print(a[-2:])
# s = " abcdefghijklmnopqrstuvwxyz "
#  print(s[3:10:1])  # 新语法 从 strat 到end 每隔step个元素取一个元素
# print(s[5:3:-1])

# #  大小写转换
# s = "what fuck baby forever ! "
# s1 = s.upper()
# print(s1)

# upper的实际应用 验证码
code = "aBc2"
code1 = input(f"请输入验证码（{code}）")
if code.upper() == code1.upper():
    print("验证码正确")
else:
    print("验证码错误")
#  今天就到这里 晚安！

