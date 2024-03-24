from __future__ import print_function
import torch


def test1():
    x = torch.empty(5, 3)  # 创建一个五行三列的矩阵（没有初始化）
    print(x)

    y = torch.randn(5, 3)
    # 创建一个有初始化的矩阵
    # print(y)

    # 加法操作
    # print(x+y)
    # y.add(x)
    # print(type(x))
    # 进行切片操作
    print(x[:2, :])  # 选择前两行所有内容


def test2():
    x = torch.randn(4, 4)
    print(x)

    y = x.view(16)  # 变成一维的张量
    print(y)
    # -1 代表自动匹配，不管有多少行，都变成两行
    y1 = x.view(-1, 2)
    print(y1)

    print(x.view(-1))


def test3():
    # # 得到全1的3X3矩阵
    # x1 = torch.ones(3, 3)
    # print(x1)

    # 创建一个带有回溯功能的矩阵，具有梯度功能
    x = torch.ones(3, 3, requires_grad=True)
    y = x.sum()
    # print(x)
    # print(x.grad_fn)  # 打印回溯函数
    # print(y.grad_fn)
    # print(y)
    y.backward()
    print(x.grad)
    # 撤下计算图方法一
    x.detach()
    # 方法二
    with torch.no_grad():
        pass
    



if __name__ == '__main__':
    # test1()
    # test2()
    test3()
