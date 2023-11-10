# # 函数的定义
# def 函数的名字():
#     code
# # 函数的调用
# 函数的名字()

# def suzhisanlian():
#     print("哦")
#     print("甚善")
#     print("都行")
#     print("收工")
# def suzhiliulian():  # 函数的嵌套
#     suzhisanlian()
#     suzhisanlian()
# suzhiliulian()

# 四则运算计算器函数版
def calculate(a, opt, b):
    if opt == "+":
        print(a + b)
    elif opt == "-":
        print(a - b)
    elif opt == "*":
        print(a * b)
    elif opt == "/":
        print(a / b)
    else:
        print("输入值格式无效")


(c) = int(input("请输入"))
(o) = input("请输入")
(d) = int(input("请输入"))
calculate(c, o, d)
# 今天就到这里晚安
