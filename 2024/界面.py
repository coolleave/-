from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton, QFileDialog


class ChatDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        # 初始化ui界面
        self.file_button = QPushButton("选择文件")  # 创建上传文件按钮控件
        # 绑定按钮点击信号和槽函数
        self.file_button.clicked.connect(self.handle_select_file)

        # 聊天记录
        self.history = QTextEdit()
        self.history.setReadOnly(True)  # 设置只读属性

        # 设置垂直布局器
        file_layout = QVBoxLayout()
        file_layout.addWidget(self.file_button)  # 放入上传文件按钮

        # 设置输入布局器
        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()  # 创建输入框
        self.send_button = QPushButton("发送")  # 发送按钮

        # 绑定发送按钮信号和槽函数
        self.send_button.clicked.connect(self.handle_send_message)
        self.input_box.returnPressed.connect(self.handle_send_message)
        input_layout.addWidget(self.input_box)  # 添加输入框
        input_layout.addWidget(self.send_button)  # 添加发送按钮

        # 创建总体布局容器
        main_layout = QVBoxLayout()
        main_layout.addLayout(file_layout)  # 放入文件上传布局
        main_layout.addWidget(self.history)  # 放入聊天记录布局
        main_layout.addLayout(input_layout)  # 添加输入按钮布局

        # 设置总体布局
        self.setLayout(main_layout)

        # 初始化聊天记录
        self.chat_history = []

    # 处理发送的信息
    def handle_send_message(self):
        # 赋值输入信息
        message = self.input_box.text()
        # 清除输入信息
        self.input_box.clear()
        # 展示‘我’ 发送的信息
        self.display_message(("我: " + message).rjust(93 - len(message)))  # 设置右对齐
        # 展示 系统回复的信息
        response = self.get_response(message)
        self.display_message("AI: " + response)

    # 上传文件
    def handle_select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "选择文件")
        if file_path:
            pass  # todo

    def display_message(self, message):
        # 往聊天记录添加消息
        # self.chat_history.append(message)
        self.history.append(message)

    # 回复聊天信息 todo
    def get_response(self, message):
        return "你好。"

    # # 展示聊天记录
    # def show_chat_history(self):
    #     for message in self.chat_history:
    #         self.history.append(message)


if __name__ == '__main__':
    # app = QApplication([])
    #
    # dialog = ChatDialog()
    # dialog.show()
    # app.exec_()
    from PyQt5 import uic

    # 将.ui文件转换为.py文件
    with open("2.10_1.py", "w", encoding="utf-8") as py_file:
        uic.compileUi("2.10界面.ui", py_file)
