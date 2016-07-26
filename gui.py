# coding:utf-8
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from mainwindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wd = Ui_MainWindow()
    wd.show()
    app.exec_()
