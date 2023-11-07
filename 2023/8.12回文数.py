# x = 10
# if x < 0:
#     pass
# else:
#     lst1 = []
#     lst2 = []
#     x = str(x)
#     for i in range(len(x)):
#         lst1.append(x[i])
#     print(x)
#
#     for a in range(len(x)-1, -1, -1):
#         print(a)
#         lst2.append(x[a])
#
#     print(lst1, lst2)
#     lst1 = ''.join(lst1)
#     lst2 = ''.join(lst2)
#     print(lst1, lst2)
#     if lst1 == lst2:
#         print()
#     else:
#         print(2)


def second():

    x = 1000
    print(str(x))
    print(str(x)[::-1])
    return str(x) == str(x)[::-1]

print(second())