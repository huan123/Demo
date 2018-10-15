#######点击某个item，显示对应的帧
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class DumbDialog(QDialog):
    def Clicked(self,qListWidgetItem):
        ##取出data，序号为系统默认，把图片名取出来#####
        imagepath = qListWidgetItem.data(Qt.UserRole)
        #把对应的帧图片取出来
        index = imagepath.find('_')
        t = index - 4
        m = index -2

        s1 = imagepath[t:index]
        s4 = imagepath[m:index]

        print("s1")
        print(s1)
        print("s4")
        print(s4)


        s2 = "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/boundingBoxImage/"
        imagename = s2 + s1 + "_" + s4 + ".png"
        print("imagename")
        print(imagename)

        self.image = QImage(imagename)
        pixmap = QPixmap.fromImage(self.image)
        m = 300
        h = self.image.height()
        w = self.image.width()
        n = (m * w) / h
        self.imageView.setPixmap(pixmap.scaled(n, m, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))


    def __init__(self, parent=None):
        super(DumbDialog, self).__init__(parent)
        self._title = "人物检索系统"
        self._diawidth = 600
        self._diaheight = 600
        self.setWindowTitle(self._title)
        self.setMinimumHeight(self._diaheight)
        self.setMinimumWidth(self._diawidth)

        self.imageView = QLabel("")
        self.imageView.setAlignment(Qt.AlignCenter)

        self.layout = QGridLayout()
        self.layout.addWidget(self.imageView, 1, 1, 1, 1)

        image_path = "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/vedioImageEvery/0018_01.png"
        image_path2 = "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/vedioImageEvery/0021_01.png"
        image_path3 = "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/vedioImageEvery/0024_02.png"


        app = QApplication(sys.argv)
        listWidget = QListWidget()

        listWidget.resize(400, 400)
        listWidget.setIconSize(QSize(100, 100))
        listWidget.setViewMode(QListView.IconMode)
        listWidget.setSpacing(10)
        listWidget.setResizeMode(QListWidget.Adjust)
        listWidget.setMovement(QListView.Static)

        image1 = QPixmap(image_path)
        item = QListWidgetItem()
        item.setIcon(QIcon(image1))
        ##设置data，序号为系统默认，把图片名字存进去#####
        item.setData(Qt.UserRole,image_path)
        listWidget.addItem(item)


        image2 = QPixmap(image_path2)
        item = QListWidgetItem()
        item.setIcon(QIcon(image2))
        item.setData(Qt.UserRole,image_path2)

        listWidget.addItem(item)

        image3 = QPixmap(image_path3)
        item = QListWidgetItem()
        item.setIcon(QIcon(image3))
        item.setData(Qt.UserRole,image_path3)
        listWidget.addItem(item)

        listWidget.addItem("Item 4");

        listWidget.itemClicked.connect(self.Clicked)
        self.layout.addWidget(listWidget, 2, 2, 2, 2)
        self.setLayout(self.layout)

        self.show()
        sys.exit(app.exec_())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    global dia
    dia = DumbDialog()
    dia.show()
    app.exec_()


