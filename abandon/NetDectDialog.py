# coding:utf-8
import nmap
from PyQt5 import QtCore, QtWidgets, Qt
from DbInputDialog import *
from PyQt5.Qt import *
from scripts import *
import Global_list
from DBConfigurations import *
import re


class NetDectDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NetDectDialog, self).__init__()
        self.setWindowTitle(u"Database Detect")
        self.resize(700, 500)

        self.dbconn = DBConfigurations()

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 700, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizentalLayout = QtWidgets.QHBoxLayout()
        self.horizentalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizentalLayout.setSpacing(6)

        self.label1 = QtWidgets.QLabel(u"Network Segment")
        self.netedit = QtWidgets.QLineEdit()
        self.btnDet = QtWidgets.QPushButton(u"Scan")
        self.btnDet.setStyleSheet(
            Global_list.BTN_STYLE)

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
        self.detresult.setColumnCount(3)
        self.detresult.setHorizontalHeaderLabels([u"IP Address", u"Database", u"Version"])
        self.detresult.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.detresult.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.detresult.horizontalHeader().setStretchLastSection(True)
        self.detresult.setContextMenuPolicy(Qt.CustomContextMenu)
        self.detresult.customContextMenuRequested.connect(self.displayContextMenu)
        self.detresult.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.conMenu = QtWidgets.QMenu()
        self.action1 = QtWidgets.QAction(u"Add Databse Target", self.conMenu)
        self.action1.triggered.connect(self.menuActivate)

        self.horizontalLayout_progressBar = QtWidgets.QHBoxLayout()
        self.horizontalLayout_progressBar.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_progressBar.setSpacing(6)
        self.progress = QtWidgets.QProgressBar()
        self.progress.setRange(0, 100)
        self.horizontalLayout_progressBar.addWidget(self.progress)
        self.verticalLayout.addLayout(self.horizontalLayout_progressBar)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.btnconfirm = QtWidgets.QPushButton(u"Confirm")
        self.btnconfirm.setStyleSheet(
            Global_list.BTN_STYLE)
        self.horizontalLayout_3.addWidget(self.btnconfirm)
        self.btncancel = QtWidgets.QPushButton(u"Cancel")
        self.horizontalLayout_3.addWidget(self.btncancel)
        self.btncancel.setStyleSheet(
            Global_list.BTN_STYLE)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btncancel.clicked.connect(self.reject)
        self.btnconfirm.clicked.connect(self.accept)

        self.btnDet.clicked.connect(self.detectNewWork)
        self.autofodun = {}

    def displayScanres(self):
        self.detresult.setRowCount(0)
        rowcount = 0
        self.autofunList = []
        for catagory in self.autofodun:
            for item in self.autofodun[catagory]:
                rowcount = rowcount + 1
                self.autofunList.append(item)
                self.detresult.setRowCount(rowcount)
                item1 = QtWidgets.QTableWidgetItem(item[0])
                item2 = QtWidgets.QTableWidgetItem(item[1])
                item3 = QtWidgets.QTableWidgetItem(item[2])
                self.detresult.setItem(rowcount - 1, 0, item1)
                self.detresult.setItem(rowcount - 1, 1, item2)
                self.detresult.setItem(rowcount - 1, 2, item3)

    def accept(self):
        QtWidgets.QDialog.accept(self)
        print "accept"

    def reject(self):
        QtWidgets.QDialog.reject(self)
        print "reject"

    def detectNewWork(self):
        print "Detect"
        ipgroupstr = self.netedit.text()
        if (re.match("^(?:(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))$",
                     ipgroupstr) == None):
            QMessageBox.information(self, u"Incorrect IP Format", u"Only Support IPv4", QMessageBox.Ok)
            return
        lst = ipgroupstr.split(".")
        print lst[0], lst[1], lst[2]
        nm = nmap.PortScanner()
        hoststring = '%s.%s.%s.1/24' % (lst[0], lst[1], lst[2])
        print hoststring
        self.progress.setValue(15)
        nm.scan(hosts=str(hoststring), ports="1433,3306,1433")
        hosts = nm.all_hosts()
        self.autofodun.clear()
        self.autofodun['mysql'] = []
        self.autofodun['sqlserver'] = []
        self.autofodun['oracle'] = []
        for item in hosts:
            tcpitem = nm[item]['tcp']
            if nm[item].has_tcp(3306):
                if tcpitem[3306]['state'] == 'open':
                    self.autofodun['mysql'].append((item, tcpitem[3306]['product'], tcpitem[3306]['version']))
            if nm[item].has_tcp(1433):
                if tcpitem[1433]['state'] == 'open':
                    self.autofodun['sqlserver'].append((item, tcpitem[1433]['product'], tcpitem[1433]['version']))
            if nm[item].has_tcp(1521):
                if tcpitem[1521]['state'] == 'open':
                    self.autofodun['oracle'].append((item, tcpitem[1521]['product'], tcpitem[1521]['version']))

        self.finishDet()
        self.displayScanres()

    def finishDet(self):
        self.progress.setValue(100)

    def nmapcallback(self, host, res):
        self.scanresult.append(res)
        print host
        print res

    def displayContextMenu(self, pos):
        self.conMenu.addAction(self.action1)
        self.conMenu.exec_(QCursor.pos())

    def menuActivate(self):
        inputDlg = DBInputDialog()
        rowindex = self.detresult.currentIndex().row()
        inputDlg.setDBIp(self.autofunList[rowindex][0])
        dbtype = self.autofunList[rowindex][1]
        print dbtype
        dbtypeint = 0
        if (re.match("[mysql MariaDB]", dbtype) != None):
            dbtypeint = 2
        elif (re.match("[microsoft sql server]") != None):
            dbtypeint = 1
        else:
            dbtypeint = 0
        inputDlg.setDBtype(dbtypeint)
        inputDlg.setDBTypeVersion(self.autofunList[rowindex][2])
        if inputDlg.exec_() == QtWidgets.QDialog.Accepted:
            self.dbconn.addDB(inputDlg.getDataBaseDefines())
        inputDlg.destroy()
