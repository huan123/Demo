#-*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
    QSizePolicy, QLabel, QFontDialog, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.my_UI()

    def my_UI(self):
        #vbox = QVBoxLayout()
        self.btn = QPushButton('选择字体', self)
        self.btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.lbl = QLabel("好好学习，天天向上",self)
        self.lbl.move(120,20)

        self.setGeometry(300, 300, 290, 250)
        self.setWindowTitle('输入对话')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()#为啥把ex去掉之后，就不显示对话框了
    sys.exit(app.exec_())


