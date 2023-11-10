"""
装饰器格式
def wrapper():
    def inner(*args **kwargs):
    #  *args 接收所有的位置参数 以元组的形式储存  **kwargs 接收所有的关键字参数 以字典的形式储存
        ####
        fn(*args **kwargs)
    # *args 将元组打散成位置参数传入 **kwargs 将字典打散成关键字参数传入
        ####
    return inner

"""


def dg(classes):
    def inner(*args, **kwargs):
        print('打开钉钉，签到')
        classes(*args, **kwargs)
        print('关闭钉钉')
    return inner


@dg
def cla(*args, **kwargs):
    print(*args, **kwargs)


cla(134235, 2354234, '语文')
