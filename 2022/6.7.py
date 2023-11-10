dic = {"圣锤之毅": "波比", "蛮族之王": "泰达米尔",
       "祖安狂人": "蒙多", "无双剑姬": "菲奥娜",
       "外壳1": {"2": "最终结果"}}
# 字典的循环 for循环
# for key in dic:  # 字典循环默认拿到的是key
#     print(key, dic[key])  # 通过key再去拿value

# 也可以通过dic.keys/values/items直接拿到元素
# 输出的方式是<class 'dict_items'>
# print(dic.values())
# print(dic.keys())  # 通过keys可以直接拿到所有的key
# print(type(dic.items()))

# 补充知识点
# a, b = (1, 2)
# print(a)
# print(b)

# 最简单的字典拿键值对的循环
# for key, value in dic.items():
#     print(key, value)

# 字典的循环嵌套 和列表一样 嵌套的索引也和列表一样
print(dic["外壳1"]["2"])


#  字典的删除不能直接删除 需要使用临时列表法进行删除

