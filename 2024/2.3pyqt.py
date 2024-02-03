import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QLineEdit, QDesktopWidget
from PyQt5.QtGui import QIcon  # 设置程序icon导入的函数


def test1():
    app = QApplication(sys.argv)
    w = QWidget()
    # 设置标题
    w.setWindowTitle('user login')
    w.setGeometry(300, 300, 300, 125)
    button_login = QPushButton('login', w)
    label_un = QLabel('uersname:', w)
    label_pw = QLabel('password:', w)
    line_un = QLineEdit(w)
    line_pw = QLineEdit(w)
    label_un.setGeometry(40, 40, 100, 20)
    label_pw.setGeometry(40, 0, 100, 20)
    line_un.setGeometry(100, 0, 100, 20)
    line_pw.setGeometry(100, 40, 100, 20)
    button_login.setGeometry(120, 100, 50, 30)
    # 将窗口放到屏幕中间显示
    # 找到屏幕中心坐标
    center_point = QDesktopWidget().availableGeometry().center()
    # 拿到x y坐标
    x = center_point.x()
    y = center_point.y()
    # 移动窗口
    w.move(x-150, y-75)
    # 拿到宽高
    weight = w.frameGeometry().getRect()[2]
    hight = w.frameGeometry().getRect()[3]
    # 移动窗口
    w.move(x - weight//2, y - hight//2)  # 必须用int，所以用整除
    # 设置程序icon
    w.setWindowIcon(QIcon('龙卡通.png'))

    w.show()
    app.exec()




if __name__ == '__main__':
    test1()
