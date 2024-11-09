"""
Author: guo yawen
Date: 2021-05-29 01:06:14
LastEditTime: 2021-05-29 02:02:08
LastEditors: guo yawen
Description: 
FilePath: /workplace/whut_daka_gui.py
TrafalgarSX
"""


import sys
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QToolTip,
    QWidget,
)
from whut_daka import *


class Example(QWidget):

    """Docstring for Example."""

    def __init__(self):
        """TODO: to be defined.

        :Docstring for Example.: TODO

        """
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QtGui.QFont("SansSerif", 10))
        self.setToolTip("Execute daka program")

        btn = QPushButton("Execute", self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        btn.clicked.connect(self.buttonClicked)

        out_info = QLabel("Response")
        self.out_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(btn, 1, 0)

        grid.addWidget(out_info, 2, 0)
        grid.addWidget(self.out_edit, 2, 1, 2, 1)

        self.setLayout(grid)
        self.resize(800, 600)
        self.setWindowTitle("WHUT daka GUI")

    def center(self):
        qr = self.frameGeometry()
        # cp = QDesktopWidget().availableGeometry().center()
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox()
        reply.setText("Are you sure to quit?")
        reply.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )

        x = reply.exec()
        if x == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def buttonClicked(self):
        self.out_edit.setText(
            # wutao() + "\n" + guoyawen() + "\n" + zhang() + "\n" + chu()
            zhang()
        )
        self.out_edit.append("成功打卡！！！")


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
