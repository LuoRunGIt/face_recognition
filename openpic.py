import sys

import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import camera5
from PyQt5.QtCore import *


class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(600, 400)
        self.setWindowTitle("label显示图片")

        self.label = QLabel(self)
        self.label.setText("   显示图片")
        self.label.setFixedSize(480, 320)
        self.label.move(60, 60)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(255,255,255);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        print(imgName)
        new_image=camera5.Face_Detect_Pic(imgName)
        cv2.imwrite("1.jpg",new_image)
        jpg = QtGui.QPixmap("./1.jpg").scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
    # camera5.Face_Detect_Pic()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
