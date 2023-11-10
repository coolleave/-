# 文件的读取
# a = open("文件操作相关素材.txt", 'r', encoding='UTF-8')
# content = a.read()  # read 为读取全部
# print(content)

# content = a.readline().strip()  # 读取文件的一行
# print(content)
# content = a.readline().strip()  # 读取文件的下一行
# print(content)
# content = a.readlines()  # 默认拿出所有的行放进列表里 输入数字可以指定几行
# print(content)


# 最重要的读取文本的方式
# for s in a:
#     print(s.strip())

# 文件的写入
# f = open("方圆几里", 'w', encoding="utf-8")
# f.write("别只有发泄那么幼稚")
# f.close()  # 没次操作完程序 尽量关闭链接

# 小练习 准备一个列表 把列表的内容写入到文件当中
lis = ['许嵩', '徐良', '汪苏泷', '薛之谦']
f = open("方圆几里", 'w', encoding='utf-8')
for i in range(len(lis)):
    f.write(lis[i])
    f.write("\n")
print(f)
f.close()

# 今天就到这里 晚安！

