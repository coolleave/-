import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.input_box = None
        self.history = None

        self.setupUi()
        # 初始化聊天记录
        self.chat_history = []
        # 聊天记录显示

    def setupUi(self):

        self.resize(561, 534)
        self.setWindowTitle('界面')
        self.setWindowIcon(QIcon('logo.png'))

        # 设置外部容器
        container = QtWidgets.QVBoxLayout(self)

        # 设置聊天记录
        self.history = QtWidgets.QTextEdit()
        # 设置样式
        self.history.setStyleSheet("background-color: white;\n"
                                   "    color: black;\n"
                                   "    border: 2px solid #4080ff;\n"
                                   "    border-radius: 10px;\n"
                                   "    padding: 10px 20px;\n"
                                   "    font-family: Arial;\n"
                                   "    font-size: 16px;\n"
                                   "    text-align: center;\n"
                                   "    text-decoration: none;\n"
                                   "    qproperty-icon: url(:/images/icon.png);")
        # 设置聊天记录只读读性
        self.history.setReadOnly(True)

        # 添加聊天记录框到外层容器
        container.addWidget(self.history)

        # 设置水平容器容纳两个按钮和输入框
        h_layout = QtWidgets.QHBoxLayout()

        btn_load = QtWidgets.QPushButton(self)
        btn_load.setText('上传文件')
        btn_load.setStyleSheet("background-color: white;\n"
                               "    color: black;\n"
                               "    border: 2px solid #4080ff;\n"
                               "    border-radius: 10px;\n"
                               "    padding: 10px 20px;\n"
                               "    font-family: Arial;\n"
                               "    font-size: 12px;\n"
                               "    text-align: center;\n"
                               "    text-decoration: none;\n"
                               "    qproperty-icon: url(:/images/icon.png);")

        h_layout.addWidget(btn_load)

        # 创建输入框
        self.input_box = QtWidgets.QLineEdit()
        self.input_box.setPlaceholderText('请输入内容...')
        self.input_box.setStyleSheet("background-color: white;\n"
                                     "    color: black;\n"
                                     "    border: 2px solid #4080ff;\n"
                                     "    border-radius: 10px;\n"
                                     "    padding: 10px 20px;\n"
                                     "    font-family: Arial;\n"
                                     "    font-size: 16px;\n"
                                     "    text-align: center;\n"
                                     "    text-decoration: none;\n"
                                     "    qproperty-icon: url(:/images/icon.png);")

        h_layout.addWidget(self.input_box)

        btn_send = QtWidgets.QPushButton()
        btn_send.setText('发送')
        btn_send.setStyleSheet("background-color: white;\n"
                               "    color: black;\n"
                               "    border: 2px solid #4080ff;\n"
                               "    border-radius: 10px;\n"
                               "    padding: 10px 20px;\n"
                               "    font-family: Arial;\n"
                               "    font-size: 12px;\n"
                               "    text-align: center;\n"
                               "    text-decoration: none;\n"
                               "    qproperty-icon: url(:/images/icon.png);")

        # 水平布局器中添加发送按钮
        h_layout.addWidget(btn_send)
        # 将水平布局器添加到容器中
        container.addLayout(h_layout)

        # 绑定按钮点击信号和槽函数
        btn_load.clicked.connect(self.handle_select_file)
        btn_send.clicked.connect(self.handle_send_message)
        self.input_box.returnPressed.connect(self.handle_send_message)

    # 上传文件
    def handle_select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择文件")
        if file_path:
            pass  # todo

    # 处理发送的信息
    def handle_send_message(self):
        # 赋值输入信息
        message = self.input_box.text()
        # 清除输入信息
        self.input_box.clear()
        # 展示‘我’ 发送的信息
        self.display_message(("我: " + message).rjust(105 - len(message)))  # 设置右对齐
        # 展示 系统回复的信息
        response = self.get_response(message)
        self.display_message("AI: " + response)

    def display_message(self, message):
        # 往聊天记录添加消息
        # self.chat_history.append(message)
        self.history.append(message)

    # 回复聊天信息 todo
    def get_response(self, message):
        return "你好。"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_Form()
    w.show()
    app.exec()
