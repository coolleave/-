# 小题一道 将列表 [1, 2, 3, 4] 每一个元素后边加上3个0


lst = [1, 2, 3, 4]
lst1 = [0 for i in range(16)]
lst1[::4] = lst  # 关键步骤
print(lst1)
