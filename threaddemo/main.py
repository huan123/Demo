
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from thread import Thread
##负责application########
from PyQt5.QtWidgets import *

import sys

class ThreadingTutorial(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # self._diawidth = 1500
        # self._diaheight = 800
        #

    def show_text(self):
        self.textEdit.setText("我是自定义线程")
        imagefilename = QFileDialog.getOpenFileName(self, "OpenFile",
                                                    "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/imageQuery",

                                                    "Image Files(*.MTS *.jpg *.png)")

        print("imagefilename1")

        print(imagefilename)

        imagefilename1 = "".join(tuple(imagefilename))
        imagefilename = imagefilename1[0:-30]
        print("imagefilename")

        print(imagefilename)
        image = QImage()
        if imagefilename != "":
            image = QImage(imagefilename)

            scene = QGraphicsScene()
            pixmap = QPixmap.fromImage(image)

            #默认加载比例
            scene.addPixmap(pixmap).setScale(0.5)
            self.graphicsView.setScene(scene)
            self.graphicsView.resize(150, 200)
            self.graphicsView.show()


    def done(self):
        self.textEdit.setText("内置线程：我是系统线程完成后的done函数")
    def test(self):
        self.textEdit.setText("我是按钮点击事件，设置文本值")
        self.thread = Thread()
        self.thread.start()

        #使用自定义信号
        self.thread.show_text.connect(self.show_text)
        #使用系统信号
        self.thread.finished.connect(self.done)

    def on_pushButton_released(self):
        self.test()




def main():
    app = QApplication(sys.argv)
    form = ThreadingTutorial()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
