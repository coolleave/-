#  今天学习字典 以键值对形式储存数据的
#  字典的表示方法dic = {key: value， key2: value2}
dic = {"英语": "文科", "物理": "理科"}
# print(dic["英语"])  # 字典中数据的拿取就和列表的索引差不多
#  字典的key必须是可哈希的数据类型（不可改变的） value可以是任何的数据类型
# print(dic)
dic['cpy'] = 'ypc'
# print(dic)

a = input("请输入")
val = dic.get(a)
if val is None:
    print("输入无效")
else:
    print(val)


# # 字典的查询
# print(dic.get('cpy12'))  # 如果没有key就会返回none
# print(dic['cpy1'])  # 如果没有key程序就会报错
