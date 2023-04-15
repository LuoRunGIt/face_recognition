import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel


class MyWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MainWindow")
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        layout = QHBoxLayout()
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Jump")
        self.btn.clicked.connect(self.jump)
        _1 = QLabel(self)
        _1.setText(" " * 5)
        _2 = QLabel(self)
        _2.setText(" " * 5)
        layout.addWidget(_1)
        layout.addWidget(self.btn)
        layout.addWidget(_2)
        self.setLayout(layout)

    def jump(self):
        child = DialogOfYouNeed()
        child.exec_()


class ChildDialogUi(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowCloseButtonHint)
        layout = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setText("This is child dialog.")
        layout.addWidget(self.label)
        self.setLayout(layout)


class DialogOfYouNeed(ChildDialogUi):
    def __init__(self):
        super().__init__()

        # write down you logic code here


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
