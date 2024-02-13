import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QApplication


class Ui_ui(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        # 设计ui界面
        self.resize(398, 265)
        self.setStyleSheet("QPushButton {\n"
                            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4CAF50, stop:1 #45a049);\n"
                            "    border: none;\n"
                            "    color: white;\n"
                            "    padding: 10px 20px;\n"
                            "    text-align: center;\n"
                            "    text-decoration: none;\n"
                            "    display: inline-block;\n"
                            "    font-size: 16px;\n"
                            "    margin: 4px 2px;\n"
                            "    cursor: pointer;\n"
                            "    border-radius: 5px;\n"
                            "}\n"
                            "\n"
                            "QPushButton:hover {\n"
                            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #45a049, stop:1 #4CAF50);\n"
                            "}\n"
                            "\n"
                            "QPushButton:pressed {\n"
                            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #379e3b, stop:1 #3d8b3d);\n"
                            "    border-style: inset;\n"
                            "}")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 70, 209, 81))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)

        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.btn_single = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_single.setText('single')
        self.horizontalLayout.addWidget(self.btn_single)
        self.btn_mult = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_mult.setStyleSheet("")
        self.btn_mult.setText('mult')
        self.horizontalLayout.addWidget(self.btn_mult)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 绑定信号槽
        self.btn_single.clicked.connect(self.btn_single_click)
        self.btn_mult.clicked.connect(self.btn_mult_click)

    def btn_single_click(self):
        for i in range(10):
            print(i)
            time.sleep(1)

    def btn_mult_click(self):
        # 创建并执行线程
        self.thread = Mythread()
        self.thread.start()


# 创建子线程类
class Mythread(QThread):
    # 继承父类
    def __init__(self):
        super().__init__()

    # 功能方法
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Ui_ui()
    dialog.show()
    app.exec_()
