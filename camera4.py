# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # self.set(CV_CAP_PROP_FPS,30)
        self.openFlag=0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cm_lab = QtWidgets.QLabel(self.centralwidget)
        self.cm_lab.setGeometry(QtCore.QRect(40, 50, 381, 321))
        self.cm_lab.setText("")
        self.cm_lab.setObjectName("cm_lab")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(620, 100, 75, 23))
        self.openBtn.setObjectName("openBtn")
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setGeometry(QtCore.QRect(620, 150, 75, 23))
        self.closeBtn.setObjectName("closeBtn")

        # 按钮绑定函数
        self.openBtn.clicked.connect(self.opencm)
        self.closeBtn.clicked.connect(self.closecm)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        self.menu_demo = QtWidgets.QMenu(self.menubar)
        self.menu_demo.setObjectName("menu_demo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_demo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openBtn.setText(_translate("MainWindow", "开启"))
        self.closeBtn.setText(_translate("MainWindow", "关闭"))
        self.menu_demo.setTitle(_translate("MainWindow", "简易的摄像头demo"))

    def opencm(self):
        # sender=self.sender()
        print("open", self.cap)
        self.openFlag=1
        while (self.openFlag==1):
            if self.cap.isOpened() == False:
                print('can not open camera')
                break
            flag, self.image = self.cap.read()
            # 这样写只显示一个图片

            show = cv2.resize(self.image, (480, 320))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.cm_lab.setPixmap(QPixmap.fromImage(showImage))
            # self.camera.open()
            # flag,self.image=self.camera.cap.read()
            # show=cv2.resize(self.image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
        self.cap = cv2.VideoCapture(0)

    def closecm(self):
        self.openFlag=0
        # self.camera.close()
        print("close", self.cap)
        self.cap.release()
        self.cm_lab.clear()
        # 这里需要重新给摄像头赋值，否则会移除
        self.cap = cv2.VideoCapture(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 使用sys新建一个应用（Application）对象
    MainWindow = QMainWindow()  # 新建一个Qt中QMainWindow()类函数
    ui = Ui_MainWindow()  # 定义ui，与我们设置窗体绑定
    ui.setupUi(MainWindow)  # 为MainWindow绑定窗体
    MainWindow.show()  # 将MainWindow窗体进行显示
    sys.exit(app.exec_())