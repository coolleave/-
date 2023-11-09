# i = 1 #项数
# s = 1  #首项
# while i <= 68: #确定循环及其范围
#     print(s) #输出项求和sn
#     i = 2*i  #每一项与前一项的关系
#     s = s+i  # 项数累加
# n = 1
# s = 1
# while n <= 68:
#     print (s)
#     n = n + 1
#     s = n**2

# n = 1
# #  项数从第一个开始
# a = -n ** (n-1)
# # 首项为1
# s = 0
# while n <= 100 :
#     s = a+s
#     n = n + 1
#     a = n * -1 ** (n - 1)
# print(s)

# a = "旁叶易寒哈哈哈"
# for c in a: #在a中为c赋值
#     print("你是谁啊" + c)

# for a in range(2,10):
#     # 从所选范围中为a赋值，注意 这里的范围不包括10 所以只是到9
#     print(a)
#
# for i in range(5,9,2):
#     print(i)

# a = 0
# b = bool(a)
# print(b)
while 1 :                    # 循环条件
    content = input("你要喷的内容")      # 输入内容
    if content:                         # 如果有内容
        print("发送给下路" + content)     # 输出
        print("发送给下路" + content)     # 输出


