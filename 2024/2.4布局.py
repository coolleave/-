import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QStackedLayout, QLabel
from PyQt5.QtCore import Qt


# 模拟登录界面
def test1():
    class Window(QWidget):
        def __init__(self):
            super(Window, self).__init__()
            self.init_ui()

        def init_ui(self):

            self.setWindowTitle('登录界面')
            # 设置固定窗口大小（不可拉伸）
            self.setFixedSize(300, 150)
            # 创建容器
            container = QVBoxLayout()

            # 创建表单布局器
            form = QFormLayout()

            # 创建第一个输入框
            edit_un = QLineEdit()
            edit_un.setPlaceholderText('请输入账号')
            form.addRow('账号:', edit_un)

            # 创建第二个输入框
            edit_un = QLineEdit()
            edit_un.setPlaceholderText('请输入密码')
            form.addRow('密码:', edit_un)

            container.addLayout(form)

            # 创建登录按钮
            btn_login = QPushButton('登录')
            btn_login.setFixedSize(100, 30)

            # 把按钮添加到容器中，并且指定它的对齐方式
            container.addWidget(btn_login, alignment=Qt.AlignRight)

            self.setLayout(container)

    # 启动
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()


# 抽屉布局
def test2():
    class Window(QWidget):
        def __init__(self):
            super().__init__()

            # 设置窗口标题
            self.setWindowTitle('抽屉布局')

            # 创建抽屉布局
            self.stack = QStackedLayout()

            self.create_stacklayout()  # 创建抽屉布局函数
            self.init_ui()

        def create_stacklayout(self):

            # 分别创建两个抽屉要显示的内容
            win1 = Window1()
            win2 = Window2()
            # 添加到抽屉布局中
            self.stack.addWidget(win1)
            self.stack.addWidget(win2)

        def init_ui(self):
            # 设置窗口大小
            self.setFixedSize(300, 270)
            # 创建总体布局
            container = QVBoxLayout()

            # 创建显示框部分
            win = QWidget()
            win.setLayout(self.stack)
            # 设置显示框样式
            win.setStyleSheet("background-color:grey;")

            # 创建两个按钮部分
            btn1 = QPushButton('按钮1')
            btn2 = QPushButton('按钮2')
            # 给两个按钮创建链接,添加点击事件， 即点击后调用函数.
            # 这步是重点，按钮和抽屉界面连接的地方
            # 因为connect只能调用函数，所以使用lambda函数
            btn1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
            btn2.clicked.connect(lambda: self.stack.setCurrentIndex(1))

            # 将显示框添加到容器中
            container.addWidget(win)
            # 将按钮添加到总布局器中
            container.addWidget(btn1)
            container.addWidget(btn2)

            # 展示抽屉布局
            self.setLayout(container)

    class Window1(QWidget):
        def __init__(self):
            super().__init__()
            QLabel('我是按钮1显示的内容', self)
            self.setStyleSheet("background-color:red;")

    class Window2(QWidget):
        def __init__(self):
            super().__init__()
            QLabel('我是按钮2显示的内容', self)
            self.setStyleSheet("background-color:green;")

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()


if __name__ == '__main__':
    test2()
