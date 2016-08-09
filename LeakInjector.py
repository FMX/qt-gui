from DBConfigurations import *
from DbModifyDialog import *
from ExecutionDlg import *
from NetDectDialog import *
from TypeParser import *


class LeakInjector(QMainWindow):
    def __init__(self):
        super(LeakInjector, self).__init__()


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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = LeakInjector()
    ui.show()
    app.exec_()
