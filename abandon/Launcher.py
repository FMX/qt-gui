# coding:utf-8

import sys

from Mainwindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wd = Ui_MainWindow()
    wd.show()
    app.exec_()
