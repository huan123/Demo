
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from baseline.detect import evaluate1
from baseline.vedioFrameImage import vedioFrame
import os
import sys
class Qlist(QListWidget):
    def Clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

class DumbDialog1(QDialog):
    global image
    #image = '/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata/imageTest/0608_02.png'
    def __init__(self,  parent = None):
        super(DumbDialog1,  self).__init__(parent)
        self._title = "image_loader"
        self._diawidth = 1500
        self._diaheight = 800
        self.setWindowTitle(self._title)
        self.setMinimumHeight(self._diaheight)
        self.setMinimumWidth(self._diawidth)

        #self.title = QLabel("先选择要查询的照片")
        videoWidget = QVideoWidget()

        self.imageView = QLabel("")
        self.imageView.setAlignment(Qt.AlignCenter)

        self.imageShow = QLabel()
        self.imageShow.setAlignment(Qt.AlignCenter)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(videoWidget)

        self.btn_openimage = QPushButton("打开图片")
        self.btn_openimage.clicked.connect(self.on_btn_openimage_clicked)

        self.btn_imagesearch = QPushButton("图片检索")
        self.btn_imagesearch.clicked.connect(self.on_btn_imagesearch_clicked)

        self.btn_going = QLabel("请开始吧")

        self.btn_openvedio = QPushButton("打开视频")
        self.btn_openvedio.clicked.connect(self.on_btn_openvedio_clicked)

        self.btn_vedioselect = QPushButton("视频检索")
        self.btn_vedioselect.clicked.connect(self.on_btn_vedioselect_clicked)

        self.layout = QGridLayout()
        self.layout.addWidget(self.imageView, 1, 1, 2, 2)
        self.layout.addWidget(self.imageShow,1, 3, 2, 2)
        self.layout.addWidget(videoWidget, 1, 5, 2, 2)
        self.layout.addWidget(self.btn_openimage, 3, 1, 1, 1)
        self.layout.addWidget(self.btn_imagesearch, 3, 2, 1, 1)
        self.layout.addWidget(self.btn_going, 3, 3, 1, 2)
        self.layout.addWidget(self.btn_openvedio, 3, 5, 1, 1)
        self.layout.addWidget(self.btn_vedioselect, 3, 6, 1, 1)

        #listWidget = QListWidget()
        listWidget = Qlist()
        listWidget.resize(400, 400)
        listWidget.setIconSize(QSize(100, 300))
        listWidget.setViewMode(QListView.IconMode)
        listWidget.setSpacing(10)
        listWidget.setResizeMode(QListView.Adjust)
        listWidget.setMovement(QListView.Static)

        DATASET = '/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/mydata'
        TEST = os.path.join(DATASET, 'imageEvery')

        for image_name in os.listdir(TEST):
            if image_name == '.DS_Store':
                continue
            image_path = os.path.join(TEST, image_name)
            image1 = QPixmap(image_path)
            item = QListWidgetItem()
            item.setIcon(QIcon(image1))
            listWidget.addItem(item)
        listWidget.itemClicked.connect(listWidget.Clicked)
        self.layout.addWidget(listWidget, 4, 1, 3, 6)
        self.setLayout(self.layout)
        self.show()

    #global image
    @pyqtSlot(bool)
    def on_btn_openimage_clicked(self, checked):
        self.imagefilename = QFileDialog.getOpenFileName(self, "OpenFile", ".",
                                                    "Image Files(*.MTS *.jpg *.png)")[0]
        print("image" + self.imagefilename)
        # detect()
        # evaluate1()
        if len(self.imagefilename):
            global image
            image = self.imagefilename
            self.image = QImage(self.imagefilename)

            m = 200

            pixmap = QPixmap.fromImage(self.image)
            self.imageView.setPixmap(pixmap.scaled(m,m, Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
            self.resize(self.image.width(), self.image.height())

    @pyqtSlot(bool)
    def on_btn_imagesearch_clicked(self, checked):
        print("开始查找执行evaluate,查找匹配相似的人")
        global image
        A = evaluate1(self.imagefilename,1)
        print("执行完毕evalute1")
        #listWidget = QListWidget()
        listWidget = Qlist()
        listWidget.resize(400, 400)
        listWidget.setIconSize(QSize(100, 300))
        listWidget.setViewMode(QListView.IconMode)
        listWidget.setSpacing(10)
        listWidget.setResizeMode(QListView.Adjust)
        listWidget.setMovement(QListView.Static)
        print("开始循环输出A[i][0]")
        count = len(A)

        for i in range(count):
            print("A[i][0]")
            print(A[i][0])
            print("A[i][1]")
            print(A[i][1])
            # if A[i][1] > 34 and A[i][1] < 39:
            if A[i][1] < 100:
                image1 = QPixmap(A[i][0])
                item = QListWidgetItem()
                item.setIcon(QIcon(image1))
                listWidget.addItem(item)
        listWidget.itemClicked.connect(listWidget.Clicked)
        self.layout.addWidget(listWidget, 4, 1, 3, 6)
        self.setLayout(self.layout)
        self.show()

    @pyqtSlot(bool)
    def on_btn_vedioselect_clicked(self, checked):
        print("开始执行读取视频")
        vedioFrame(self.vediofilename)
        print("视频读取帧完成")
        #global A
        global image
        #A = evaluate1(image,2)
        A = evaluate1(image,2)
        #####3for循环显示多张图片########
        #listWidget = QListWidget()
        listWidget = Qlist()
        listWidget.resize(400, 400)
        listWidget.setIconSize(QSize(100, 300))
        listWidget.setViewMode(QListView.IconMode)
        listWidget.setSpacing(10)
        listWidget.setResizeMode(QListView.Adjust)
        listWidget.setMovement(QListView.Static)

        print("开始循环输出A[i][0]")
        count = len(A)

        for i in range(count):
            print("A[i][0]")
            print(A[i][0])
            print("A[i][1]")
            print(A[i][1])

            if A[i][1] < 100:
                image1 = QPixmap(A[i][0])
                item = QListWidgetItem()
                item.setIcon(QIcon(image1))
                listWidget.addItem(item)
        listWidget.itemClicked.connect(listWidget.Clicked)
        # self.layout.addWidget(listWidget, 4, 1, 4, 4)
        self.layout.addWidget(listWidget, 4, 1, 3, 6)
        self.setLayout(self.layout)
        self.show()


    @pyqtSlot(bool)
    def on_btn_openvedio_clicked(self, checked):
        self.vediofilename = QFileDialog.getOpenFileName(self, "OpenFile", ".",
            "Image Files(*.MTS *.mp4 *.png)")[0]
        global  vedio
        vedio = self.vediofilename
        print("vedio" + vedio)

        if len(self.vediofilename):
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(self.vediofilename)))
            self.mediaPlayer.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dia = DumbDialog1()
    dia.show()
    app.exec_()




# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
#
# import sys
# class DumbDialog1(QListWidget):
#     def Clicked(self, item):
#         QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())
# class M(QDialog):
#     def __init__(self, parent=None):
#         image_path = "/Users/huan/code/PycharmProjects/Unsupervised-Person-Re-identification-Clustering-and-Fine-tuning-master/images/demo.jpg"
#         app = QApplication(sys.argv)
#         listWidget = DumbDialog1()
#         listWidget.resize(300, 120)
#         listWidget.addItem("Item 1");
#         image1 = QPixmap(image_path)
#         item = QListWidgetItem()
#         item.setIcon(QIcon(image1))
#         listWidget.addItem(item)
#         listWidget.addItem("Item 2");
#         listWidget.addItem("Item 3");
#
#         listWidget.addItem("Item 4");
#
#         listWidget.setWindowTitle('PyQT QListwidget Demo')
#         listWidget.itemClicked.connect(listWidget.Clicked)
#
#         listWidget.show()
#         sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dia = M()
#     dia.show()
#     app.exec_()



