# n = int(input("请输入行数"))
# a = []
# for i in range(n):
#     a.append([])
#     for k in range(i+1):
#         if k == 0 or k == i:
#             a[i].append(1)
#         else:
#             a[i].append(a[i-1][k]+a[i-1][k-1])
#     print(a[i])

a = []
n = int(input('请输入行数'))
for i in range(n):
    a.append([])
    for k in range(i+1):
        if k == 0 or k == i:
            a[i].append(1)
        else:
            a[i].append(a[i-1][k]+a[i-1][k-1])
    print(a[i])
