# print("今天的学习马上开始了 加油 旁叶易寒")
# if input("请输入y继续") == "y":
#     print("首先来了解strip这个函数 他的意思是去除左右两边的空白符")
#     if input("输入y继续") == "y":
#         print("空白符包括 空格 /t /n 比如在输入用户名和密码时候经常会用到")
#         print("下面看个小案例")


while True:
    username = input("请输入用户名").strip()
    if username == "admin":
        password = input("请输入密码").strip()
        if password == "12345":
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("登陆失败")

# s = "太年轻的人，他总是不满足"
# s1 = s.replace("年轻", "老")
# print(s1)

# a = "sorry i am so sorry"
# a1 = a.replace(" ","")  # 去掉所有的空格
# print(a1)

# a = "旁叶易寒，于彭尘，哈哈哈哈"
# lst = a.split("，")  # 括号里的事用什么且 注意用什么切就会损失什么
# print(lst)
# print(lst[2])
#   #  今天就到这里 晚安
