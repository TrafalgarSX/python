import sys

# import essential dependence
from PyQt6.QtWidgets import (
    QApplication,
    QColorDialog,
    QComboBox,
    QFileDialog,
    QFrame,
    QLabel,
    QMainWindow,
    QTextEdit,
    QPushButton,
    QToolTip,
    QMessageBox,
    QMenu,
    QLCDNumber,
    QVBoxLayout,
    QSlider,
    QInputDialog,
    QFontDialog,
    QCheckBox,
    QProgressBar,
)
from PyQt6.QtGui import QAction, QFont, QIcon, QColor, QPixmap
from PyQt6.QtCore import QBasicTimer, Qt
from pathlib import Path


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # tooltip 气泡框  设置字体
        QToolTip.setFont(QFont("SansSerif", 10))
        # 创建气泡提示框 可以使用富文本内容
        self.setToolTip("This is a <b>QMainWindow</b> ")
        # 使用QMainWindow创建状态栏 并调用showMessage方法在状态栏上显示一条消息
        self.statusBar().showMessage("Ready")

        # 菜单项对应的操作和对应的shortcut
        # Qaction 是行为抽象类，包括菜单栏，工具栏或自定义键盘快捷方式
        exitAct = QAction(QIcon("maaya.jpg"), "&Exit", self)
        exitAct.setShortcut("Ctrl+W")
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(QApplication.instance().quit)

        # 菜单项
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        # fileMenu.addAction(exitAct)

        # 子菜单
        impMenu = QMenu("Import", self)
        impAct = QAction("Import mail", self)
        impMenu.addAction(impAct)

        newAct = QAction("New", self)

        fileMenu.addAction(newAct)  # 显示在子菜单中
        fileMenu.addMenu(impMenu)  # 也显示在子菜单中

        # menu checkbox
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")
        viewMenu = menubar.addMenu("View")

        viewStatAct = QAction("View statusbar", self)  # , checkable=True)
        viewStatAct.setStatusTip("View statusbar")
        viewStatAct.setCheckable(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        # QCheckBox
        cb = QCheckBox("Show title", self)
        cb.move(100, 700)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        # 进度条
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(100, 800, 200, 25)

        self.button_bar = QPushButton("Start", self)
        self.button_bar.move(100, 700)
        self.button_bar.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        # 下拉框
        combo = QComboBox(self)
        list = ["Apple", "Banana", "Orange"]
        for fruit in list:
            combo.addItem(fruit)

        combo.move(100, 600)

        combo.textActivated.connect(self.onActivated)

        # 工具栏
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAct)

        # LCDNumber  类似于音量控制器的控件
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Orientation.Horizontal, self)
        lcd.move(500, 500)
        sld.move(500, 400)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        # 对话框
        self.button_dialog = QPushButton("对话框", self)
        self.button_dialog.clicked.connect(self.showDiaglog)
        self.button_dialog.move(800, 500)

        self.button_color = QPushButton("颜色选择框", self)
        self.button_color.clicked.connect(self.showDiaglog)
        self.button_color.move(900, 500)

        self.button_font = QPushButton("字体选择框", self)
        self.button_font.clicked.connect(self.showDiaglog)
        self.button_font.move(1000, 500)

        # 文件选择框
        openFile = QAction("Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.triggered.connect(self.showFileDialog)

        openFileMenu = QMenu("打开文件", self)
        openFileMenu.addAction(openFile)
        fileMenu.addMenu(openFileMenu)

        # 可选颜色对话框
        self.frm = QFrame(self)
        col = QColor(0, 0, 0)
        self.frm.setStyleSheet("QWidget { background-color:%s }" % col.name())
        self.frm.setGeometry(600, 600, 200, 200)

        # 字体选择框 设置
        self.lbl = QLabel("Knowledge only matters", self)
        self.lbl.move(1000, 1000)

        self.editor_gbk = QTextEdit(self)
        self.editor_gbk.setGeometry(30, 60, 280, 200)
        self.button_gbk = QPushButton("show utf8", self)
        self.button_gbk.setToolTip("This is a <b>Buttion</b> ")

        self.button_gbk.setGeometry(330, 120, 100, 30)
        self.button_gbk.clicked.connect(self.convert_gbk_to_utf8)

        self.editor_utf8 = QTextEdit(self)
        self.editor_utf8.setGeometry(30, 280, 280, 200)

        # quit buttion
        self.button_quit = QPushButton("quit", self)
        self.button_quit.setGeometry(900, 100, 100, 30)
        self.button_quit.clicked.connect(QApplication.instance().quit)

        # set mainwindows position and size: x y w h
        # self.setGeometry(100, 100, 1000, 1000)
        self.resize(1400, 1000)
        self.center()
        self.setWindowTitle("Converter")

    def convert_utf8_to_gbk(self):
        utf8_text = self.editor_utf8.toPlainText()
        try:
            gbk_text = utf8_text.encode("utf-8").decode("gbk")
            self.editor_gbk.setPlainText(gbk_text)
        except Exception as e:
            self.editor_gbk.setPlainText("translate wrong")

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Message",
            "Are you sure to quit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        # 得到一个矩形的窗口
        qr = self.frameGeometry()
        # 屏幕属性里计算出分辨率，然后计算出中心点位置
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        # 把应用窗口的左上方点坐标移动到矩形窗口的左上方,这样就可以居中显示了
        self.move(qr.topLeft())

    """
    该函数功能并不是将gbk编码的字符转为 utf8编码
    该函数的功能其实是 将原本是utf8编码（错误显示为gbk）的字符用utf8编码展示
    """

    def convert_gbk_to_utf8(self):
        gbk_text = self.editor_gbk.toPlainText()
        try:
            utf8_text = gbk_text.encode("gbk").decode("utf-8")
            self.editor_utf8.setPlainText(utf8_text)
        except Exception as e:
            self.editor_utf8.setPlainText("translate wrong")
            # raise e

    def toggleMenu(self, state):
        if state:
            self.editor_utf8.setPlainText("成功")
            self.statusbar.show()
        else:
            self.editor_utf8.setPlainText("")
            self.statusbar.hide()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("new")
        openAct = cmenu.addAction("open")
        quitAct = cmenu.addAction("quit")
        action = cmenu.exec(self.mapToGlobal(event.pos()))

        if action == quitAct:
            QApplication.instance().quit()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def buttonClicked(self):
        sender = self.sender()

        msg = f"{sender} clicked"
        self.statusBar().showMessage(msg)

    def showDiaglog(self):
        sender = self.sender()

        if sender == self.button_dialog:
            text, ok = QInputDialog.getText(self, "Input Dialog", "Enter text:")

            if ok:
                self.editor_gbk.setPlainText(str(text))
        elif sender == self.button_color:
            col = QColorDialog.getColor()
            if col.isValid():
                self.frm.setStyleSheet("QWidget { background-color:%s }" % col.name())
        elif sender == self.button_font:
            font, ok = QFontDialog.getFont()
            if ok:
                self.lbl.setFont(font)
            pass

    def showFileDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, "Open file", home_dir)
        if fname[0]:
            f = open(fname[0], "r", encoding="utf-8")

            with f:
                data = f.read()
                self.editor_gbk.setPlainText(data)

    def changeTitle(self, state):
        if state == Qt.CheckState.Checked.value:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle("")

    def changeValue(self, value):
        if value == 0:
            self.lbl.setPixmap(QPixmap("maaya.jpg"))
        elif 0 < value <= 30:
            self.lbl.setPixmap(QPixmap("maaya.jpg"))
        if 30 < value < 80:
            self.lbl.setPixmap(QPixmap("maaya.jpg"))
        else:
            self.lbl.setPixmap(QPixmap("maaya.jpg"))

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.button_bar.setText("Finished")
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button_bar.setText("Start")
        else:
            self.timer.start(100, self)
            self.button_bar.setText("Stop")

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        pass


def main():
    # every PyQt6 program has to create a QApplication object
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
