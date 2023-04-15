import layin
import sys

if __name__ == '__main__':
    app = layin.QApplication(sys.argv)  # 使用sys新建一个应用（Application）对象
    MainWindow = layin.QMainWindow()  # 新建一个Qt中QMainWindow()类函数
    ui = layin.Ui_MainWindow()  # 定义ui，与我们设置窗体绑定
    ui.setupUi(MainWindow)  # 为MainWindow绑定窗体
    MainWindow.show()  # 将MainWindow窗体进行显示
    sys.exit(app.exec_())
