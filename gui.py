# coding:utf-8

import sys

from mainwindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wd = Ui_MainWindow()
    wd.show()
    app.exec_()
