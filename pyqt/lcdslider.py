import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import (QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication)
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.my_UI()

    def my_UI(self):

        lcd = QLCDNumber(self)
        #通过该语句我们创建了一个水平滑块部件
        sld = QSlider(Qt.Horizontal,self)
        #垂直布局
        vbox = QVBoxLayout()

        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('信号 & 槽')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

