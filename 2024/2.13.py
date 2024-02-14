import json
import time
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import requests


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("2.13.ui")
        # print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # 提取要操作的控件
        self.user_name = self.ui.lineEdit_uersname  # 用户名输入框
        self.password = self.ui.lineEdit_password  # 密码输入框
        self.login_btn = self.ui.btn_login  # 登录按钮
        self.forget_password_btn = self.ui.btn  # 忘记密码按钮
        self.textBrowser = self.ui.textEdit  # 文本显示区域

        # 绑定信号与槽函数
        self.login_btn.clicked.connect(self.login_btn_click)

        self.log_thread = Login_Thread()  # 创建子线程
        self.log_thread.signal.connect(self.log_thread.login_request)
        self.log_thread.start()  # 执行子线程


    def login_btn_click(self):
        name = self.user_name.text()
        password = self.password.text()
        dic = {'name': name, 'password': password}
        self.log_thread.signal.emit(json.dumps(dic))
        # print(type(json.dump({'name': name, 'password': password})))


class Login_Thread(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            print('子线程正在执行')
            time.sleep(1)

    def login_request(self, ua_pw):
        ua_pw_json = json.loads(ua_pw)
        username = ua_pw_json.get('name')
        password = ua_pw_json.get('password')
        # print(username, password)
        print(ua_pw_json)
        resp = requests.post(url='https://service-2yxjqwel-1324305345.bj.tencentapigw.com.cn/release/qt_login', json=ua_pw_json)
        # text = resp.content.decode = 'utf-8'
        print(resp.content.decode('unicode_escape'))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()

    app.exec()

