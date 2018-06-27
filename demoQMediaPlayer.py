from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
class VideoWindow(QDialog):
    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("PyQt Video Player Widget Example - pythonprogramminglanguage.com")

        videoWidget = QVideoWidget()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.playButton = QPushButton("播放",self)
        self.playButton.clicked.connect(self.play)

        self.openButton = QPushButton("打开视频")
        self.openButton.clicked.connect(self.openFile)

        #一种布局
        self.layout = QVBoxLayout()
        self.layout.addWidget(videoWidget)
        self.layout.addWidget(self.playButton)
        self.layout.addWidget(self.openButton)

        self.setLayout(self.layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.show()

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.mediaPlayer.play()
    def play(self):
        self.mediaPlayer.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())

