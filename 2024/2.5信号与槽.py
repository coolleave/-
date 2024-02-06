"""
模块导入顺序
1、系统模块
2、第三方库
3、自定义模块

"""
import sys
import time

from PyQt5.QtWidgets import QApplication,  QWidget, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def test1():
    class Window(QWidget):
        def __init__(self):
            super(Window, self).__init__()
            self.init_ui()

        def init_ui(self):
            self.setWindowTitle('信号与槽')
            btn = QPushButton('点我', self)
            self.setFixedSize(300, 200)
            self.setStyleSheet("background-color:gray;")
            btn.clicked.connect(lambda argv: print("我被点了", argv))

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()


def test2():
    class Window(QWidget):
        # 声明一个信号变量，变量只能在类属性里
        signal = pyqtSignal(str)

        def __init__(self):
            super(Window, self).__init__()
            self.init_ui()

        def init_ui(self):
            self.resize(500, 200)
            self.setWindowTitle('安全检测')
            # 创建布局管理器
            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignCenter)  # 设置居中

            btn = QPushButton('开始检测')
            layout.addWidget(btn)

            btn.clicked.connect(self.btn_click)
            self.signal.connect(lambda msg: print(f'>>> {msg}'))
            self.setLayout(layout)

        def btn_click(self):
            for i, ip in enumerate([f"192.168.1.{x}" for x in range(1, 255)]):
                msg = "模拟，正在检查 %s 上的漏洞...." % ip
                # print(msg)
                if i % 5 == 3:
                    # 表示发射信号 对象.信号.发射(参数)
                    self.signal.emit(msg + "【发现漏洞】")
                time.sleep(0.01)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()


# 发送网络模拟测试（应用滚动条）
def test3():
    class Window(QWidget):
        signal = pyqtSignal(str)

        def __init__(self):

            super().__init__()
            self.init_ui()
            self.msg_list = list()  # 用来存放消息

        def init_ui(self):
            self.resize(500, 200)
            # 创建垂直布局容器
            container = QVBoxLayout()

            # 创建标签
            self.msg = QLabel('')
            self.msg.setWordWrap(True)
            self.msg.resize(300, 15)
            self.msg.setAlignment(Qt.AlignTop)  # 靠上
            # self.msg.setStyleSheet("backgroself.msg = QLabel('')und-color: yellow; color: black;")

            # 创建滚动条
            scroll = QScrollArea()
            scroll.setWidget(self.msg)

            # 创建垂直布局器，用来添加自动滚动条
            v_layout = QVBoxLayout()
            v_layout.addWidget(scroll)

            # 创建第二部分按钮
            btn = QPushButton('开始检测')
            # 创建水平布局
            h_layout = QHBoxLayout()

            h_layout.addStretch(1)  # 设置弹簧，让按钮水平居中
            h_layout.addWidget(btn)
            h_layout.addStretch(1)

            btn.clicked.connect(self.click)

            # 添加两个布局器到容器里
            container.addLayout(v_layout)
            container.addLayout(h_layout)
            self.setLayout(container)

            # 绑定信号和槽
            self.signal.connect(self.solt)

        def click(self):
            # 通过enumerte(), 拿到索引和值
            for i, ip in enumerate([f'196.128.1.{x}'] for x in range(1, 100)):

                if i % 5 == 3:
                    msg = "模拟，正在检查 %s 上的漏洞...." % ip[0]
                    # print(msg)

                    self.signal.emit(msg + '发现漏洞')
                    time.sleep(0.1)

        def solt(self, msg):
            print(msg)
            self.msg_list.append(msg)
            # print(self.msg_list)
            # 用换行符<br>拼接列表
            self.msg.setText("<br>".join(self.msg_list))
            self.msg.resize(440, self.msg.frameSize().height() + 15)
            self.msg.repaint()  # 更新内容，如果不更新可能没有显示新内容

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()


if __name__ == '__main__':
    test3()
