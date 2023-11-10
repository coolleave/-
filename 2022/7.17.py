# def computer(*zj):  # *表示动态传参 就是可以输入多个参数
#     print(zj)
#
#
# computer("cpu", "gpu", "nc",)


# def func(a, b, *args, c=3, **kwargs):  # 形参的总结 正确顺序
#     print(a, b, c, args, kwargs)
#
#
# func(1, 2, 4, 5, 6, 7, cpy="leave")


peo_list = ["张三", "李四", "王二麻子", "小萝卜头"]

def ren(*args):
    print(args)


ren()
