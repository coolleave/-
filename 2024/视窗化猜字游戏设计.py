import sys  # 导入系统组件
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import random  # 导入随机数模块


# 创建类 猜数游戏
class GuessNumberGame(QWidget):
    def __init__(self):
        # 继承父类的初始化方法
        super().__init__()
        # 设置标题
        self.setWindowTitle("猜字游戏")
        # 设置窗口大小和位置
        self.setGeometry(300, 300, 600, 400)

        # 设置目标函数随机数
        self.target_number = random.randint(0, 10000)

        # 输入提示标签框并绑定给主窗口
        self.guess_label = QLabel("输入你的猜测:", self)

        # 输入框
        self.guess_input = QLineEdit(self)

        # 猜数按钮
        self.guess_button = QPushButton("猜!", self)

        # 准备输出提示
        self.result_label = QLabel("", self)

        # 设置垂直布局作为容器
        layout = QVBoxLayout()
        # 将以上的组件添加到容器中
        layout.addWidget(self.guess_label)
        layout.addWidget(self.guess_input)
        layout.addWidget(self.guess_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # 将按钮的信号与函数槽绑定
        self.guess_button.clicked.connect(self.check_guess)

    # 检查函数槽
    def check_guess(self):
        # 将猜的数字修改为输入框内容
        guess = self.guess_input.text()
        # 进行猜数判定
        try:
            guess = int(guess)
            if guess == self.target_number:
                self.result_label.setText(f"恭喜你猜中了！数字是: {self.target_number}")
                self.guess_button.setEnabled(False)  # 禁用按钮
            elif guess < self.target_number:
                self.result_label.setText("猜的数字太小了！")
            else:
                self.result_label.setText("猜的数字太大了！")
        # 整数判定
        except ValueError:
            self.result_label.setText("请输入一个整数！")
        # 清除猜数框
        self.guess_input.clear()
        # 设置焦点优先级
        self.guess_input.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = GuessNumberGame()
    game.show()
    sys.exit(app.exec_())
