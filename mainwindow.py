# coding:utf-8
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from DBConfigurations import *
from DbInputDialog import *
from NetDectDialog import *


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.connectSlotsAndFuncs()

    def setupUi(self, MainWindow):
        self.setObjectName("MainWindow")
        self.resize(672, 508)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 671, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btnNetDet = QtWidgets.QPushButton(self.verticalLayoutWidget)
        # self.btnNetDet=AeroButton(self.verticalLayoutWidget)
        self.btnNetDet.setObjectName("btnNetDet")
        self.btnNetDet.setStyleSheet(
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.horizontalLayout.addWidget(self.btnNetDet)

        self.btnAddDB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAddDB.setObjectName("btnAddDB")
        self.btnAddDB.setStyleSheet(
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.horizontalLayout.addWidget(self.btnAddDB)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.lstDBs = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.lstDBs.setObjectName("lstDBs")

        self.horizontalLayout_2.addWidget(self.lstDBs)
        self.lstLeks = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.lstLeks.setObjectName("lstLeks")

        self.horizontalLayout_2.addWidget(self.lstLeks)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.setCentralWidget(self.centralWidget)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.btnExec = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExec.setStyleSheet(
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.btnExec.setObjectName("btnExec")

        self.horizontalLayout_3.addWidget(self.btnExec)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 672, 42))
        self.menuBar.setObjectName("menuBar")

        self.menuFILE = QtWidgets.QMenu(self.menuBar)
        self.menuFILE.setObjectName("menuFILE")

        self.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")

        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")

        self.setStatusBar(self.statusBar)
        self.actionEXIT = QtWidgets.QAction(MainWindow)
        self.actionEXIT.setObjectName("actionEXIT")

        self.menuFILE.addAction(self.actionEXIT)
        self.menuBar.addAction(self.menuFILE.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", u"主窗口"))
        self.btnNetDet.setText(_translate("MainWindow", u"网络发现"))
        self.btnAddDB.setText(_translate("MainWindow", u"添加数据库"))
        self.btnExec.setText(_translate("MainWindow", u"执行攻击"))
        self.menuFILE.setTitle(_translate("MainWindow", "FILE"))
        self.actionEXIT.setText(_translate("MainWindow", "EXIT"))

    def connectSlotsAndFuncs(self):
        self.btnNetDet.clicked.connect(self.netDet)
        self.btnAddDB.clicked.connect(self.addDB)
        self.btnExec.clicked.connect(self.execute)

    def addDB(self):
        print 'adddb'
        input = DBInputDialog(self)
        if input.exec_():
            print input.dbservertypcmb.itemText(input.dbservertypcmb.currentIndex())

        input.destroy()

    def netDet(self):
        print "netdet"
        netdet = NetDectDialog(self)
        if netdet.exec_():
            print "test"
        netdet.destroy()

    def execute(self):
        print "execute"
