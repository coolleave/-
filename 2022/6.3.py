#  sort() 列表的排序
# lst = [3, 4, 1, 3, 5]
# lst.sort()
# print(lst)
# lst.sort(reverse=True)  #  reverse 翻转 倒叙
# print(lst)

# lst = ["石钟山记", "归去来兮辞", "种树郭橐驼传", "a","2"]
# lst.append("孙悟空")  #
# lst.sort()
# print(lst)
# #  列表的嵌套
# lst = [2, 4, 5, ["fsf", "reat"]]
# print(lst[-1][1])

# 正确
lst = ["刘波", "陈子昂", "刘明智", "顾森系", "吴悦城", "郭天祥", "刘桂英"]
temp = []
for i in range(len(lst)):
    item = lst[i]
    if lst[i].startswith("刘"):
        temp.append(lst[i])
for a in temp:
    lst.remove(a)
print(lst)


print(lst)


# #  删除列表中所有姓张的
# lst = ["刘波", "陈子昂", "刘明智", "顾森系", "吴悦城", "郭天祥", "刘桂英"]
# temp = []  #  储存一个临时列表来备用
# for itme in lst:
#     if itme.startswith("刘"): # 找出要删除的元素
#         temp.append(itme)   #加入到临时列表里先不要着急删除
# for it in temp:
#     lst.remove(it)  #删除临时列表里的文件
# print(lst)

#今天就到这里 晚安


