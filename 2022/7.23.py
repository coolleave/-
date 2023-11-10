#  闭包函数
def func():
    a = 13

    def inner():
        nonlocal a
        a = a+1
        print(a)
        return a
    return inner


ret = func()
ret()

