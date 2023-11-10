# s = "北海的天平开始倾斜，季节已变迁"
# for a in s:  #复习for in
#     print(a)

# s = "海市蜃楼"
# print(len(s))  #输出字符串中有多少字元素
# lst = ["薛之谦", "周润发", "刘德华"]
# print(len(lst))
# lst = ["chen"]
# print("chen" in lst)

#  append 追加列表 在列表的最后一个元素中追加一个
# lst = ["大头儿子", "小头爸爸", "哈皮父子"]
# lst.append("果宝特攻")
# print(lst)

# lst = ["chen", "peng", "yu"]
# ret = lst.pop(2)
# print(ret)
# print(lst)

# #  小练习把所有的列表元素改成大写
# lst = ["for", "top", "student", "from", "family", "the"]
# for item in lst:
#     new_item = item.upper()
#     print(new_item)

#  小练习讲列表中所有姓刘的人改成姓萧的人
lst = ["刘波", "陈子昂", "刘明智", "顾森系", "吴悦城", "郭天祥", "刘桂英"]
print(f"改之前的名字{lst}")
for i in range(len(lst)):
    item = lst[i]
    if item.startswith("刘"):
        lst[i] = "萧" + item[1::]
print(f"修改后的名字{lst}")
#  今天就到这里 晚安！


