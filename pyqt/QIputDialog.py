#-*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.my_UI()

    def my_UI(self):
        self.btn = QPushButton('选择字体', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 250)
        self.setWindowTitle('输入对话')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, '输入对话',
                                        '输入你的名字:')
        # 这一行会显示一个输入对话框。第一个字符串参数是对话框的标题，
        # 第二个字符串参数是对话框内的消息文本。对话框返回输入的文本
        # 内容和一个布尔值。如果我们点击了Ok按钮，布尔值就是true，反
        # 之布尔值是false（也只有按下Ok按钮时，返回的文本内容才会有值）。
        if ok:
            self.le.setText(str(text))  # 把从对话框接收到的文本设置到单行编辑框组件上显示。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()#为啥把ex去掉之后，就不显示对话框了
    sys.exit(app.exec_())


