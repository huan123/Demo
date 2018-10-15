import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.my_UI()

    def my_UI(self):

        self.textEdit = QTextEdit()  # 增加文本编辑器
        self.setCentralWidget(self.textEdit)  # 设置为中心布局
        self.statusBar()  # 增加状态栏

        openFile = QAction(QIcon('open.png'), '打开', self)  # 增加打开文件动作
        openFile.setShortcut('Ctrl+O')  # 连接快捷键
        openFile.setStatusTip('打开新文件')  # 显示状态栏提示
        openFile.triggered.connect(self.showDialog)  # 触发则连接showDialog方法

        menubar = self.menuBar()  # 增加菜单栏
        fileMenu = menubar.addMenu('&文件')  # 增加菜单
        fileMenu.addAction(openFile)  # 菜单里增加动作

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('文件对话框')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/Users/huan/code/PycharmProjects/PedestrianDetection')
        # 弹出文件选择框
        # 第一个字符串参数是getOpenFileName()方法的标题。第二个字符串参数
        # 指定了对话框的工作目录。默认的，文件过滤器设置成All files (*)。
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

        # 选中文件后，读出文件的内容，并设置成文本编辑框组件的显示文本

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    

