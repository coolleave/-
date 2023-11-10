# 装饰器的通式
# def wrapper(fn):
#     def inner(*args, **kwargs):
#         pass
#         ret = fn(*args, **kwargs)
#         pass
#         return ret
#     return inner
#
#
# @wrapper
# def target():
#     pass
#
#
# #  装饰器的叠加问题
# def wrapper1(fn):
#     def inner(*args, **kwargs):
#         print("1进")
#         ret = fn(*args, **kwargs)
#         print("1出")
#         return ret
#     return inner
#
#
# def wrapper2(fn):
#     def inner(*args, **kwargs):
#         print('2进')
#         ret = fn(*args, **kwargs)
#         print('2出')
#         return ret
#     return inner
#
#
# @wrapper1
# @wrapper2
# def func():
#     print('self')
#
#
# func()


# # 装饰器实战  员工信息录入系统
# login = False
#
#
# def login_verity(fn):
#     def inner(*args, **kwargs):
#         global login
#         if not login:
#             while True:
#                 print('还没有登录')
#                 username = input('请输入用户名>>>')
#                 password = input('请输入密码>>>')
#                 if username == 'admin' and password == '123':
#                     print('登录成功')
#                     login = True
#                     break
#                 else:
#                     print('登陆失败，用户名或密码错误')
#         ret = fn(*args, **kwargs)
#         return ret
#     return inner
#
#
# @login_verity
# def add():
#     print('增加员工信息')
#
#
# @login_verity
# def delete():
#     print('删除员工信息')
#
#
# @login_verity
# def upd():
#     print('修改员工信息')
#
#
# @login_verity
# def search():
#     print('查询员工信息')
#
#
# add()
# delete()
# upd()
# search()

from urllib.request import urlopen
url = 'http://121.26.242.250:8001/srcja.asp?dhhm1=aaaa'
resp = urlopen(url)
print(resp.read().decode('gbk'))
