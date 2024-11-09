import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.editor_gbk = QTextEdit(self)
        self.editor_gbk.setGeometry(10, 10, 280, 200)
        self.button_gbk = QPushButton("show utf8", self)
        self.button_gbk.setGeometry(300, 50, 100, 30)
        self.button_gbk.clicked.connect(self.convert_gbk_to_utf8)

        self.button_utf8 = QPushButton("show gbk", self)
        self.button_utf8.setGeometry(300, 100, 100, 30)
        self.button_utf8.clicked.connect(self.convert_utf8_to_gbk)

        self.editor_utf8 = QTextEdit(self)
        self.editor_utf8.setGeometry(10, 220, 280, 200)

        # self.button_utf8 = QPushButton('UTF-8', self)
        # self.button_utf8.setGeometry(300, 270, 100, 30)
        # self.button_utf8.clicked.connect(self.convert_utf8_to_gbk)

        self.setGeometry(100, 100, 500, 550)
        self.setWindowTitle("Converter")

    def convert_utf8_to_gbk(self):
        utf8_text = self.editor_utf8.toPlainText()
        try:
            gbk_text = utf8_text.encode("utf-8").decode("gbk")
            self.editor_gbk.setPlainText(gbk_text)
        except Exception as e:
            error = str(e)
            self.editor_gbk.setPlainText("translate wrong: \n" + error + "\n" + utf8_text)

    """
    该函数功能并不是将gbk编码的字符转为 utf8编码
    该函数的功能其实是 将原本是utf8编码（错误显示为gbk）的字符用utf8编码展示
    """
    def convert_gbk_to_utf8(self):
        gbk_text = self.editor_gbk.toPlainText()
        try:
            utf8_text = gbk_text.encode("gbk", 'ignore').decode("utf-8", 'replace')
            self.editor_utf8.setPlainText(utf8_text)
        except Exception as e:
            error = str(e)
            self.editor_utf8.setPlainText("translate wrong: \n" + error)
            # raise e


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
