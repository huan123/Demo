import sys
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.my_UI()

    def my_UI(self):
        # exitAction = QAction(QIcon('1.png'), '&关于钉钉', self)
        #
        # exitAction.setShortcut('Ctrl+Q')
        # #exitAction.setStatusTip('退出应用')
        # exitAction.triggered.connect(self.showDialog)
        #
        # self.statusBar()

        # 定义菜单栏，并且添加文件
        menubar = self.menuBar()
        #menubar.setNativeMenuBar(False)
        ding = menubar.addMenu('钉钉')
        about = ding.addAction('关于钉钉')
        about.triggered.connect(self.showDialog)


        preference = ding.addAction('偏好设置')
        update = ding.addAction('检查更新')
        service = ding.addMenu('服务')
        subservice1 = service.addAction('没有服务可用')
        subservice2 = service.addAction('服务偏好设置')

        hide1 = ding.addAction('隐藏钉钉')
        hide2 = ding.addAction('隐藏其他')
        showall = ding.addAction('显示全部')
        exit = ding.addAction('退出钉钉')

        #fileMenu.addAction(exitAction)
        change = menubar.addMenu('修改')
        revocation = change.addAction('撤销')
        recreation = change.addAction('重做')
        clip = change.addAction('剪贴')
        copy = change.addAction('拷贝')
        paste = change.addAction('粘贴')
        pastematch = change.addAction('粘贴并匹配样式')
        delete = change.addAction('删除')
        spell = change.addMenu('拼写和语法')
        showall = spell.addAction('显示拼写和语法')
        nowcheck = spell.addAction('立即检查文稿')
        check = spell.addAction('键入时检查拼写')
        checkspell = spell.addAction('检查拼写和语法')
        correctspell = spell.addAction('自动纠正拼写')

        replace = change.addMenu('替换')
        switch = change.addMenu('转换')
        language = change.addMenu('语音')
        dictation = change.addAction('开始听写')
        emotionandsymbol = change.addAction('表情与符号')

        windows = menubar.addMenu('窗口')
        minwindows = windows.addMenu('最小化')
        close = windows.addMenu('关闭')
        zoom = windows.addMenu('缩放')
        fullscreen = windows.addMenu('进入全屏幕')
        prepositionwindow = windows.addMenu('前置全部窗口')
        dingding = windows.addMenu('钉钉')

        help = menubar.addMenu('帮助')
        search = help.addMenu('搜索')
        dinghelp = help.addMenu('钉钉帮助')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('钉钉')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            '/Users/huan/code/PycharmProjects/PedestrianDetection')
        # 弹出文件选择框
        # 第一个字符串参数是getOpenFileName()方法的标题。第二个字符串参数
        # 指定了对话框的工作目录。默认的，文件过滤器设置成All files (*)。

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

#     # 选中文件后，读出文件的内容，并设置成文本编辑框组件的显示文本


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

