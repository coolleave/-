"""
作用域 变量的访问权限
"""


# def func1():
#     pass
#
#
# def func2():
#     func1()
#     pass
#
# # 这叫函数的调用不叫函数的嵌套
#
# def func1():
#     def func2():
#         pass
# # 这才叫函数的嵌套

# 内部函数的外部调用

# def func():
#     def func1():
#         pass
#     return func1
#
#
# ret = func()
# print(ret())

def an():
    pass


bn = an
bn(3)
