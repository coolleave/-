import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QRadioButton, QGroupBox


# 面向对象编程
def test1():
    class Window(QWidget):
        # 重写父类
        def __init__(self):
            super().__init__()  # 调用父类的初始化方法

            self.resize(300, 300)
            self.setWindowTitle('垂直布局')

            # 创建垂直布局管理器
            layout = QVBoxLayout()
            btn1 = QPushButton('按钮1')
            layout.addWidget(btn1)
            # 添加一个伸缩器 相当于弹簧。 就是相当于一个东西占位
            layout.addStretch()  # 设置比例
            btn2 = QPushButton('按钮2')
            layout.addWidget(btn2)
            layout.addStretch()
            btn3 = QPushButton('按钮3')
            layout.addWidget(btn3)
            layout.addStretch()

            self.setLayout(layout)  # 创建了布局管理器，就必须要执行

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()


def test2():
    class Window(QWidget):
        # 重写父类
        def __init__(self):
            super().__init__()  # 调用父类的初始化方法

            self.resize(300, 300)
            self.setWindowTitle('水平布局')

            # 创建垂直布局管理器
            layout = QHBoxLayout()
            btn1 = QPushButton('按钮1')
            layout.addStretch(1)
            layout.addWidget(btn1)
            # 添加一个伸缩器 相当于弹簧。 就是相当于一个东西占位
            # layout.addStretch()  # 设置比例
            btn2 = QPushButton('按钮2')
            layout.addWidget(btn2)
            # layout.addStretch()
            btn3 = QPushButton('按钮3')
            layout.addWidget(btn3)
            layout.addStretch(1)

            self.setLayout(layout)  # 创建了布局管理器，就必须要执行

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()

# 布局器的嵌套


def test3():
    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('information')
            self.init_ui()

        def init_ui(self):

            # 创建外层垂直布局器
            # container = QVBoxLayout()
            container = QHBoxLayout()
            # 创建布局器组
            hobby = QGroupBox('爱好')
            # 创建内层垂直布局器
            v_layout = QVBoxLayout()
            btn1 = QRadioButton('somke')
            btn2 = QRadioButton('drink')
            btn3 = QRadioButton('perm')
            v_layout.addWidget(btn1)
            v_layout.addWidget(btn2)
            v_layout.addWidget(btn3)
            hobby.setLayout(v_layout)

            # 创建水平布局器组
            gender = QGroupBox('性别')
            # 创建内层水平布局器
            h_layout = QHBoxLayout()

            btn4 = QRadioButton('man')
            btn5 = QRadioButton('woman')
            h_layout.addWidget(btn4)
            h_layout.addWidget(btn5)
            gender.setLayout(h_layout)

            # 把两个容器组作为控件widget添加到外层中
            container.addWidget(hobby)
            container.addWidget(gender)
            # 创建外层垂直布局器
            wrap_layout = QVBoxLayout()
            self.setLayout(container)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()


if __name__ == '__main__':
    test3()
