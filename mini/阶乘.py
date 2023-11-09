# # 任意非负整数的阶乘n!
# n = int((input('请输入一个非负整数')))
# val = 1
# if n == 0:
#     print(1)
# if n >= 1:
#     while n >= 1:
#         val = val*n
#         n = n-1
#         print(val)
# 形如
# n = int(input('请输入上标（非负整数）'))
# m = int(input('请输入下标（正整数）'))
# val_m = 1
# val_n = 1
# if m >= n >= 0:
#     if m == 0:
#         print('数据无效')
#     if n == 0:
#         if m == 0:
#             print('数据无效')
#         elif m != 0:
#             print(1)
#
# if m >= n >= 0 and n*m != 0:
#     while m > 1:
#         val_m = val_m*m
#         m = m-1
#     while n > 1:
#         val_n = val_n*n
#         n = n-1
#
#     A = int(val_m/val_n)
#     print(f'A是{A}')
# else:
#     print('数据无效')


# C的计算
while 1:
    m = int(input('请输入下标（正整数）'))
    n = int(input('请输入上标（非负整数）'))

    val1 = 1
    val2 = 1
    if n == 0 and m > 0:
        print(0)
    elif m > n > 0:
        n1 = n
        m1 = m
        while n1 > 0:
            val1 = val1*m1
            m1 = m1-1
            n1 = n1-1
        # print(val1)
        n2 = n
        while n2 > 1:
            val2 = val2*n2
            n2 = n2-1
        # print(val2)

        print(int(val1/val2))
    else:
        print('数据无效')
