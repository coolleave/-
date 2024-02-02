from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
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


if __name__ == '__main__':
    button()