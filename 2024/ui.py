import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication,  QWidget, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtWidgets import QDialog,QHBoxLayout, QTextEdit, QLineEdit


# class FileUploadApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('上传文件')
#         self.setGeometry(100, 100, 400, 200)
#
#         self.upload_button = QPushButton('Upload File', self)
#         self.upload_button.setGeometry(150, 80, 100, 30)
#         self.upload_button.clicked.connect(self.upload_file)
#
#     def upload_file(self):
#         file_dialog = QFileDialog()
#         file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'All Files (*);;Text Files (*.txt)')
#
#         if file_path:
#             print(f'File uploaded: {file_path}')


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置标题和大小
        self.setWindowTitle('界面')
        self.resize(450, 300)
        # 创建容器
        container = QVBoxLayout()
        # 创建上传文件按钮
        self.upload_button = QPushButton('Upload File')
        # 将按钮添加到容器中
        container.addWidget(self.upload_button)
        # 绑定按钮信号和槽
        self.upload_button.clicked.connect(self.upload_file)

        # 设置容器
        self.setLayout(container)

    # 上传文件槽
    def upload_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'All Files (*);;Text Files (*.txt)')

        if file_path:
            print(f'File uploaded: {file_path}')


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # mainwindow = Window()
    # mainwindow.show()
    # app.exec()
    class ChatDialog(QDialog):
        def __init__(self, parent=None):
            super().__init__(parent)

            # 初始化UI界面
            self.file_button = QPushButton("选择文件")
            self.file_button.clicked.connect(self.handle_select_file)

            self.history = QTextEdit()
            self.history.setReadOnly(True)

            file_layout = QVBoxLayout()
            file_layout.addWidget(self.file_button)

            input_layout = QHBoxLayout()
            self.input_box = QLineEdit()
            self.send_button = QPushButton("发送")
            self.send_button.clicked.connect(self.handle_send_message)
            input_layout.addWidget(self.input_box)
            input_layout.addWidget(self.send_button)

            main_layout = QVBoxLayout()
            main_layout.addLayout(file_layout)
            main_layout.addWidget(self.history)
            main_layout.addLayout(input_layout)

            self.setLayout(main_layout)

            # 初始化聊天记录
            self.chat_history = []

        def handle_send_message(self):
            message = self.input_box.text()
            self.input_box.clear()

            self.display_message("我: " + message)

            response = self.get_response(message)
            self.display_message("AI: " + response)

        def handle_select_file(self):
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getOpenFileName(self, "选择文件")
            if file_path:
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                    self.display_message("上传文件: " + file_path)
                    self.display_message(file_content)

        def display_message(self, message):
            self.chat_history.append(message)
            self.history.append(message)

        def get_response(self, message):
            # TODO: 编写获取 AI 响应的逻辑
            return "你好，我是 AI。"

        def show_chat_history(self):
            for message in self.chat_history:
                self.history.append(message)


    if __name__ == '__main__':
        app = QApplication([])

        dialog = ChatDialog()
        dialog.show_chat_history()
        dialog.show()

        app.exec_()