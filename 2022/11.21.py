#  复习一遍杨辉三角形
import time
import turtle


def title():
    text = turtle.Turtle()
    text.hideturtle()
    text.write('这是自动生成杨辉三角形数的程序', font=('楷书', 10, 'normal'))
    time.sleep(3)
    text.clear()
    text.write('输入想要得到的杨辉三角形数的行数即可得到杨辉三角形数', font=('楷书', 10, 'normal'))
    time.sleep(3)
    text.clear()
    text.write('下面请输入杨辉三角形的行数', font=('楷书', 10, 'normal'))
    time.sleep(3)
    text.clear()


def content():
    a = []
    n = int(input('请输入杨辉三角形的行数'))
    for i in range(n):
        a.append([])
        for lie in range(i+1):
            if lie == 0 or lie == i:
                a[i].append(1)
            else:
                k = a[i-1][lie-1] + a[i-1][lie]
                a[i].append(k)
        print(a[i])


if __name__ == '__main__':
    title()
    content()
