

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from threaddemo.thread import Thread
##负责application########
from PyQt5.QtWidgets import *

import sys

class ThreadingTutorial(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def show_text(self):
        self.textEdit.setText("我是自定义线程")

    def done(self):
        self.textEdit.setText("我是系统线程完成后的done函数")
    def test(self):
        self.textEdit.setText("我是按钮点击事件，设置文本值")
        self.thread = Thread()
        self.thread.start()
        #使用系统信号
        self.thread.finished.connect(self.done)
        #使用自定义信号
        self.thread.show_text.connect(self.show_text)


    def on_pushButton_released(self):
        self.test()


def main():
    app = QApplication(sys.argv)
    form = ThreadingTutorial()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
