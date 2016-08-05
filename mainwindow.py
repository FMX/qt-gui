# coding:utf-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from DbInputDialog import *
from DbModifyDialog import *
from ExecutionDlg import *
from NetDectDialog import *
from typeParser import *
from DBConfigurations import *


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupLocalVars()
        self.setupUi(self)
        self.retranslateUi(self)
        self.connectSlotsAndFuncs()

    def setupLocalVars(self):
        self.dbConnection = DBConfigurations()
        self.dbitemDict = {}

    def setupUi(self, MainWindow):
        self.setObjectName("MainWindow")
        self.resize(1000, 650)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1000, 630))
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

        self.dbmenu = QtWidgets.QMenu()
        self.action1 = QtWidgets.QAction(u"修改数据库", self.dbmenu)
        self.action1.triggered.connect(self.modifyDB)
        self.action2 = QtWidgets.QAction(u"删除数据库", self.dbmenu)
        self.action2.triggered.connect(self.delDB)

        self.lstDBs = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.lstDBs.setColumnCount(4)
        self.lstDBs.setHorizontalHeaderLabels([u"数据库名", u"IP地址", u"数据库类型", u"操作系统"])
        self.lstDBs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lstDBs.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lstDBs.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lstDBs.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lstDBs.horizontalHeader().setStretchLastSection(True)
        self.lstDBs.customContextMenuRequested.connect(self.customerMenu)
        self.initDbtable()
        self.lstDBs.setObjectName("lstDBs")

        self.horizontalLayout_2.addWidget(self.lstDBs)
        self.lstLeks = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.lstLeks.setColumnCount(4)
        self.lstLeks.setHorizontalHeaderLabels([u"漏洞名", u"数据库类型", u"操作系统", u"是否需要用户信息"])
        self.lstLeks.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lstLeks.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lstLeks.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lstLeks.horizontalHeader().setStretchLastSection(True)
        self.initLeaktable()
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
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 50, 42))
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
        dlg = DBInputDialog(self)
        if dlg.exec_() == QDialog.Accepted:
            lst = dlg.getDataBaseDefines()
            # print lst
            self.dbConnection.addDB(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8], lst[9])
        dlg.destroy()
        self.updateDBtable()

    def netDet(self):
        print "netdet"
        netdet = NetDectDialog(self)
        if netdet.exec_():
            print "test"
        netdet.destroy()

    def execute(self):
        print "execute"
        execdlg = ExecutionDlg(self)
        if execdlg.exec_():
            print "exec"
        execdlg.destroy()

    def initDbtable(self):
        print "Init DB table"
        rowcount = 0
        typepro = TypeParse()
        for row in self.dbConnection.getAllDbs():
            self.dbitemDict[rowcount] = row[0]
            print self.dbitemDict
            rowcount = rowcount + 1
            self.lstDBs.setRowCount(rowcount)
            item1 = QTableWidgetItem(row[1])
            item2 = QTableWidgetItem(row[2])
            dbtype = row[3]
            item3cont = typepro.parDBType(dbtype)
            item3 = QTableWidgetItem(item3cont)
            item4 = QTableWidgetItem(typepro.parOSType(row[5]))
            self.lstDBs.setItem(rowcount - 1, 0, item1)
            self.lstDBs.setItem(rowcount - 1, 1, item2)
            self.lstDBs.setItem(rowcount - 1, 2, item3)
            self.lstDBs.setItem(rowcount - 1, 3, item4)

    def updateDBtable(self):
        self.dbitemDict.clear()
        self.lstDBs.clear()
        rowcount = 0
        typepro = TypeParse()
        for row in self.dbConnection.getAllDbs():
            self.dbitemDict[rowcount] = row[0]
            # print self.dbitemDict
            rowcount = rowcount + 1
            self.lstDBs.setRowCount(rowcount)
            item1 = QTableWidgetItem(row[1])
            item2 = QTableWidgetItem(row[2])
            dbtype = row[3]
            item3cont = typepro.parDBType(dbtype)
            item3 = QTableWidgetItem(item3cont)
            item4 = QTableWidgetItem(typepro.parOSType(row[5]))
            self.lstDBs.setItem(rowcount - 1, 0, item1)
            self.lstDBs.setItem(rowcount - 1, 1, item2)
            self.lstDBs.setItem(rowcount - 1, 2, item3)
            self.lstDBs.setItem(rowcount - 1, 3, item4)

    def initLeaktable(self):
        print "Init leak table"

    def customerMenu(self, point):
        print "Cusotmer Menu"
        self.dbmenu.addAction(self.action1)
        self.dbmenu.addAction(self.action2)
        self.dbmenu.exec_(QCursor.pos())

    def modifyDB(self, e):
        print "Modify DB"
        dlg = DBModifyDlg(self, self.dbitemDict.get(self.lstDBs.currentIndex()), self.dbConnection)
        if dlg.exec_() == QDialog.Accepted:
            lst = dlg.getDataBaseDefines()
            print lst
            self.dbConnection.updateDB(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8], lst[9])
        dlg.destroy()
        self.updateDBtable()

    def delDB(self, e):
        print "Del DB"
        index = self.dbitemDict.get(self.lstDBs.currentIndex())
        self.dbConnection.remoteDbitem(index)
        self.updateDBtable()
