#
# while True:
#     content = input("输入要说的话（输入q键停止）")
#     if content == "q":
#         continue
#     print("你在狗叫什么" + content)
#
i = 1
# while i <= 10:  # 循环i
#     if i == 6:  # 去除本次循环的不要的项目
#         i = i + 1  # 跳到下一项目
#         continue  # 终止本次循环
#     print(i)
#     i = i + 1

while True:
    i = int(input("请输入数字"))
    if i < 10:
        print("小了")
    elif i > 10:
        print("大了！")
    elif i == 10:
        print("这才是正确答案")
        break
    else:
        print("请输入数字")
