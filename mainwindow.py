# coding:utf-8

import Global_list
from DBConfigurations import *
from DbModifyDialog import *
from ExecutionDlg import *
from NetDectDialog import *
from TypeParser import *


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
        # self.btnNetDet.setStyleSheet(
        #     '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.btnNetDet.setStyleSheet(Global_list.BTN_STYLE)
        self.horizontalLayout.addWidget(self.btnNetDet)

        self.btnAddDB = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAddDB.setObjectName("btnAddDB")
        self.btnAddDB.setStyleSheet(
            Global_list.BTN_STYLE)
        self.horizontalLayout.addWidget(self.btnAddDB)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.dbmenu = QtWidgets.QMenu()
        self.action1 = QtWidgets.QAction(u"Modify Database", self.dbmenu)
        self.action1.triggered.connect(self.modifyDB)
        self.action2 = QtWidgets.QAction(u"Delete Database", self.dbmenu)
        self.action2.triggered.connect(self.delDB)

        self.lstDBs = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.lstDBs.setColumnCount(4)
        self.lstDBs.setHorizontalHeaderLabels([u"Database Name", u"IP Address", u"Database Type", u"OS Type"])
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
        self.lstLeks.setHorizontalHeaderLabels([u"Leak Name", u"Database Type", u"OS Type", u"Password Necessary"])
        self.lstLeks.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lstLeks.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.lstLeks.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lstLeks.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
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
            Global_list.BTN_STYLE)
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
        self.setWindowTitle(_translate("MainWindow", u"Main Window"))
        self.btnNetDet.setText(_translate("MainWindow", u"Net Detect"))
        self.btnAddDB.setText(_translate("MainWindow", u"Add Database Traget"))
        self.btnExec.setText(_translate("MainWindow", u"Verify"))
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
        # print "netdet"
        netdet = NetDectDialog(self)
        if netdet.exec_() == QDialog.Accepted:
            print "Net Detect Finished!"
        netdet.destroy()
        self.updateDBtable()

    def execute(self):
        # print "execute"
        dbindex = self.lstDBs.currentIndex().row()
        leakindex = self.lstLeks.currentIndex().row()
        dbid = self.dbitemDict[dbindex]
        leakid = self.leakitems[leakindex].getid()
        execdlg = ExecutionDlg(self, dbid, leakid)
        if execdlg.exec_() == QDialog.Accepted:
            print ""
        execdlg.destroy()

    def initDbtable(self):
        # print "Init DB table"
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

    def updateDBtable(self):
        self.dbitemDict.clear()
        self.lstDBs.clear()
        self.lstDBs.setColumnCount(4)
        self.lstDBs.setHorizontalHeaderLabels([u"DataBase Name", u"IP Address", u"Database Type", u"Os Type"])
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
        # print "Init leak table"
        rowcount = 0
        self.leakitems = self.dbConnection.getAllleaks()
        for row in self.leakitems:
            rowcount = rowcount + 1
            self.lstLeks.setRowCount(rowcount)
            item1 = QTableWidgetItem(row.getLeakName())
            item2 = QTableWidgetItem(row.getdbtype())
            item3 = QTableWidgetItem(row.getDBVersion())
            item4 = QTableWidgetItem(row.getReqpwd())
            self.lstLeks.setItem(rowcount - 1, 0, item1)
            self.lstLeks.setItem(rowcount - 1, 1, item2)
            self.lstLeks.setItem(rowcount - 1, 2, item3)
            self.lstLeks.setItem(rowcount - 1, 3, item4)

    def customerMenu(self, point):
        # print "Cusotmer Menu"
        self.dbmenu.addAction(self.action1)
        self.dbmenu.addAction(self.action2)
        self.dbmenu.exec_(QCursor.pos())

    def modifyDB(self, e):
        # print "Modify DB"
        dlg = DBModifyDlg(self, self.dbitemDict.get(self.lstDBs.currentIndex()), self.dbConnection)
        if dlg.exec_() == QDialog.Accepted:
            lst = dlg.getDataBaseDefines()
            print lst
            self.dbConnection.updateDB(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8], lst[9])
        dlg.destroy()
        self.updateDBtable()

    def delDB(self, e):
        # print "Del DB"
        index = self.dbitemDict.get(self.lstDBs.currentIndex())
        self.dbConnection.removeDbitem(index)
        self.updateDBtable()
