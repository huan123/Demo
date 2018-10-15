# -*- coding:UTF-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import *
import sys

from pyqtthread.ui import Ui_MainWindow
import time
from pyqtthread.getPostsThread import getPostsThread
class MainWindow(QMainWindow, Ui_MainWindow):
    #默认构造函数
    def __init__(self, parent = None):
        #至少调用一个继承类的构造函数
        QMainWindow.__init__(self, parent)
        #其中一个继承类Ui_mainWindow含有setupUi函数，self代表MainWindow，它即含有QMainWindow的属性和方法,又含有Ui_MainWindow的属性和方法
        self.setupUi(self)
        #显示MainWindow

        self.show()

    def done(self):
        self.textEdit.setText("hahhaha")

    def showText(self,text):
        self.textEdit.setText(text)

#https://nikolak.com/pyqt-threading-tutorial/

#pyqt5里面如何使用signal
#https://stackoverflow.com/questions/41848769/pyqt5-object-has-no-attribute-connect/41851968

    def test(self):
        #定义子线程对象，默认调用init
        self.get_thread = getPostsThread()
        #start会默认执行getPostsThread类的run函数
        self.get_thread.start()

        #内置信号，当线程结束时，会收到该信号
        self.get_thread.finished.connect(self.done)
        #使用自定义信号 接受信号
        self.get_thread.show_text.connect(self.showText)

    def on_pushButton_released(self):
        self.test()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #调用构造函数
    ex = MainWindow()
    sys.exit(app.exec_())
