from PyQt5.QtCore import  QThread,pyqtSignal
import time
class getPostsThread(QThread):
    #声明一个信号
    show_text = pyqtSignal(str)
    def __init__(self):
        QThread.__init__(self)


    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(2)
        #自线程发出信号
        self.show_text.emit("我是子线程的text")
        time.sleep(2)
        print("this is run")

