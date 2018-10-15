from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class DumbDialog(QDialog):
    def __init__(self, parent=None):
        super(DumbDialog, self).__init__(parent)
        self._title = "image_loader"
        self._diawidth = 300
        self._diaheight = 450
        self.setWindowTitle(self._title)
        self.setMinimumHeight(self._diaheight)
        self.setMinimumWidth(self._diawidth)
        self.imageView = QLabel("add a image file")
        self.imageView.setAlignment(Qt.AlignCenter)
        self.btn_open = QPushButton("open")
        self.btn_open.clicked.connect(self.on_btn_open_clicked)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.imageView)
        self.vlayout.addWidget(self.btn_open)
        self.setLayout(self.vlayout)

    @pyqtSlot(bool)
    def on_btn_open_clicked(self, checked):
        self.filename = QFileDialog.getOpenFileName(self, "OpenFile", ".",
                                                    "Image Files(*.jpg *.jpeg *.png)")[0]
        if len(self.filename):
            self.image = QImage(self.filename)
            self.imageView.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(), self.image.height())