from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
import sys


def button():
    # 创建程序
    app = QApplication(sys.argv)
    # 设置控件
    w = QWidget()
    # 设置窗口标题
    w.setWindowTitle('按钮')
    but_big = QPushButton('请点击')
    but_big.setParent(w)
    but_small = QPushButton('点击')
    but_small.setParent(but_big)
    # 展示窗口
    w.show()
    # 进入循环
    app.exec()


def qlabel():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('文本框显示')

    # 创建一个纯文本对象
    label = QLabel('请输入账号', w)
    # 设置大小和位置
    # (0,0) 是位置左上角是原点， 1000，1000 是宽和高
    # 绝对定位
    label.setGeometry(50, 50, 100, 100)
    w.show()
    app.exec()


# 输入框
def lineedit():
    app = QApplication(sys.argv)
    w = QWidget()
    # 创建文本框
    line = QLineEdit(w)
    # 设置大小和位置
    line.setGeometry(30, 30, 100, 30)
    w.show()
    app.exec()


def test1():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('user login')
    w.setGeometry(300, 300, 600, 400)
    button_login = QPushButton('login', w)
    label_un = QLabel('uersname', w)
    label_pw = QLabel('password', w)
    line_un = QLineEdit(w)
    line_pw = QLineEdit(w)
    label_un.setGeometry(0, 40, 100, 20)
    label_pw.setGeometry(0, 0, 100, 20)
    line_un.setGeometry(100, 0, 100, 20)
    line_pw.setGeometry(100, 40, 100, 20)
    button_login.setGeometry(100, 100, 100, 30)
    w.show()
    app.exec()



if __name__ == '__main__':
    # button()
    # qlabel()
    # lineedit()
    test1()