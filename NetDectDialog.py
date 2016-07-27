# coding:utf-8
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import nmap.nmap


class NetDectDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NetDectDialog, self).__init__()
        self.setWindowTitle(u"数据库网络发现")
        self.resize(500, 500)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 500, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizentalLayout = QtWidgets.QHBoxLayout()
        self.horizentalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizentalLayout.setSpacing(6)

        self.label1 = QtWidgets.QLabel(u"网段")
        self.netedit = QtWidgets.QLineEdit()
        self.btnDet = QtWidgets.QPushButton(u"扫描")
        self.btnDet.setStyleSheet(
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')

        self.horizentalLayout.addWidget(self.label1)
        self.horizentalLayout.addWidget(self.netedit)
        self.horizentalLayout.addWidget(self.btnDet)
        self.verticalLayout.addLayout(self.horizentalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.detresult = QtWidgets.QTableWidget()
        self.horizontalLayout_2.addWidget(self.detresult)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.btnconfirm = QtWidgets.QPushButton(u"确定")
        self.btnconfirm.setStyleSheet(
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.horizontalLayout_3.addWidget(self.btnconfirm)
        self.btncancel = QtWidgets.QPushButton(u"取消")
        self.horizontalLayout_3.addWidget(self.btncancel)
        self.btncancel.setStyleSheet(
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btncancel.clicked.connect(self.reject)
        self.btnconfirm.clicked.connect(self.accept)

    def accept(self):
        QtWidgets.QDialog.accept(self)
        print "accept"

    def reject(self):
        QtWidgets.QDialog.reject(self)
        print "reject"