#  查找
# s = "你好啊，我叫旁叶易寒，你叫什么"
# ret = s.find("我叫")
# print(ret)
#
# ret1 = s.find("我是")
# print(ret1)

# s = "我是你爸爸"
# print("爸爸" in s)  # in查找有没有""内的元素
# print("爸爸"not in s )
#
# name = input("请输入名字")
# if name.startswith("陈"):  #  判断开头是不是陈
#     print("你姓陈")
# else :
#     print("你不姓陈")  #判断结尾是不是有宇
# if name.endswith("宇"):
#     print("你有宇")
# else :
#     print("你没有")


money = input("请输入金额")
if money.isdigit():
    print(int(money))
else:
    print("输入有误")
#今天就到这里 晚安
