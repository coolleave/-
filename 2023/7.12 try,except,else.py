# 代码的报错纠错机制
# 尝试执行的代码
try:
    a = input()
    b = input()
# 程序报错后执行的代码
except BaseException as e:
    print('出错了')

else:
    print(a + b)
# 无论是否出错，程序都会执行的代码
finally:
    print('程序结束')
