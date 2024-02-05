"""
模块导入顺序
1、系统模块
2、第三方库
3、自定义模块

"""
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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


if __name__ == '__main__':
    test2()
