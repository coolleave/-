import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.my_ui()

    def my_ui(self):
        self.setWindowTitle("mainwindow")
        self.frameSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()

    w.show()
    app.exec()
