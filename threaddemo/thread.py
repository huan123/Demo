# -*- coding: utf-8 -*-
from PyQt5.QtCore import QThread,pyqtSignal
import time

class Thread(QThread):
    show_text = pyqtSignal(str)
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(2)
        self.show_text.emit("我是自定义事件")
        time.sleep(2)

