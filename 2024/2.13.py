from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("2.13.ui")
        print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件
        self.user_name = self.ui.lineEdit_uersname  # 用户名输入框
        self.password = self.ui.lineEdit_password  # 密码输入框
        self.login_btn = self.ui.btn_login  # 登录按钮
        self.forget_password_btn = self.ui.btn  # 忘记密码按钮
        self.textBrowser = self.ui.textEdit  # 文本显示区域

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login_btn_click)

    def login_btn_click(self):
        name = self.user_name.text()
        password = self.password.text()


class Thread(QThread):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()

    app.exec()
