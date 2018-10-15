import sys
from   PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication
from  PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.my_UI()
    def my_UI(self):

        exitAction = QAction(QIcon('2.png'),'&退出',self)

        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出应用')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        #定义菜单栏，并且添加文件
        menubar = self.menuBar()
        #menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('文件&(F)')
        fileMenu.addAction(exitAction)


        self.setGeometry(300,300,300,250)
        self.setWindowTitle('菜单栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


