import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog


class FileUploadApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('上传文件')
        self.setGeometry(100, 100, 400, 200)

        self.upload_button = QPushButton('Upload File', self)
        self.upload_button.setGeometry(150, 80, 100, 30)
        self.upload_button.clicked.connect(self.upload_file)

    def upload_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'All Files (*);;Text Files (*.txt)')

        if file_path:
            print(f'File uploaded: {file_path}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_upload_app = FileUploadApp()
    file_upload_app.show()
    app.exec()