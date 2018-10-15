import sys
from   PyQt5.QtWidgets import QMainWindow,QApplication

class Example(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.my_UI()
    def my_UI(self):
        #状态栏
        self.statusBar().showMessage('一切正常')

        self.setGeometry(300,300,300,250)
        self.setWindowTitle('状态栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

