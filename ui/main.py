
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from ui.test import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    #默认构造函数
    def __init__(self, parent = None):
        #至少调用一个继承类的构造函数
        QMainWindow.__init__(self, parent)
        #其中一个继承类Ui_mainWindow含有setupUi函数，self代表MainWindow，它即含有QMainWindow的属性和方法,又含有Ui_MainWindow的属性和方法
        self.setupUi(self)
        #显示MainWindow
        self.show()

    def test(self):
        print("老头子爱吃辣条")

    def on_pushButton_released(self):
        self.test()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #调用构造函数
    ex = MainWindow()
    sys.exit(app.exec_())


