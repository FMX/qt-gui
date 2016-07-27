# coding:utf-8
import sys
from PyQt5 import QtGui, QtCore, QtWidgets


class NetDectDialog(QtWidgets.QDialog):
    def __init__(self):
        super(NetDectDialog, self).__init__()
        self.setWindowTitle(u"验证")
        self.resize(550, 600)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 550, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.resultarea = QtWidgets.QTextEdit()
