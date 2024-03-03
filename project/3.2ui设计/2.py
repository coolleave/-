import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.my_ui()

    def my_ui(self):
        # 设置标题和大小
        self.setWindowTitle("mainwindow")
        self.resize(670, 460)
        # 创建一个容器
        container = QVBoxLayout()

        # 创建标题
        hbox_title = QHBoxLayout()
        title = QLabel('多层次情感分类系统', self)
        font_title = QFont('Arial', 30)  # 创建一个字体对象，设置字体为 Arial，大小为 16
        title.setFont(font_title)
        title.adjustSize()  # 调整 Label 的大小以适应文本内容
        hbox_title.addStretch(1)
        hbox_title.addWidget(title)
        hbox_title.addStretch(1)

        # 创建提示文本
        hbox_tip = QHBoxLayout()
        tip = QLabel('选择你要运行的数据集：', self)
        tip.move(10, 100)
        font_tip = QFont('Arial', 18)
        tip.setFont(font_tip)
        hbox_tip.addWidget(tip)
        hbox_tip.addStretch(1)

        # 创建文本显示框
        hbox_load = QHBoxLayout()
        button_load = QPushButton('...', self)
        button_load.setFont(QFont('Arial', 18))
        button_load.clicked.connect(self.upload_file)
        text_input = QLineEdit()
        text_input.setFixedHeight(25)
        button_load.setFixedHeight(25)
        hbox_load.addWidget(text_input)
        hbox_load.addWidget(button_load)

        # 创建按钮区域
        hbox_button = QHBoxLayout()
        button1 = QPushButton('run', self)
        button2 = QPushButton('model', self)
        button1.setFont(QFont('Arial', 18))
        button2.setFont(QFont('Arial', 18))
        button1.setFixedHeight(30)
        button2.setFixedHeight(30)
        hbox_button.addWidget(button1)
        hbox_button.addWidget(button2)

        # 创建文本显示区域
        text_ouput = QTextEdit()

        # 把布局器添加到容器
        container.addLayout(hbox_title)
        container.addLayout(hbox_tip)
        container.addLayout(hbox_load)
        container.addLayout(hbox_button)
        container.addWidget(text_ouput)
        self.setLayout(container)

    def upload_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, '选择文件', '', 'All Files (*);;Text Files (*.txt)')  # 设置文件过滤器

        if file_path:
            print('已选择文件:', file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()

    w.show()
    app.exec()
