# coding:utf-8
import nmap
from PyQt5 import QtCore, QtWidgets, Qt
from DbInputDialog import *
from PyQt5.Qt import *
from scripts import *
import Global_list


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
        self.detresult.setHorizontalHeaderLabels([u"IP", u"数据库", u"版本"])
        self.detresult.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.detresult.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.detresult.horizontalHeader().setStretchLastSection(True)
        self.detresult.setContextMenuPolicy(Qt.CustomContextMenu)
        self.detresult.customContextMenuRequested.connect(self.displayContextMenu)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.conMenu = QtWidgets.QMenu()
        self.action1 = QtWidgets.QAction(u"添加数据库", self.conMenu)
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

        self.btnconfirm = QtWidgets.QPushButton(u"确定")
        self.btnconfirm.setStyleSheet(
            Global_list.BTN_STYLE)
        self.horizontalLayout_3.addWidget(self.btnconfirm)
        self.btncancel = QtWidgets.QPushButton(u"取消")
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
        # print self.autofodun
        rowcount = 0
        print self.autofodun
        self.autofunList = {}
        for catagory in self.autofodun:
            for item in self.autofodun[catagory]:
                rowcount = rowcount + 1
                # print item
                self.autofunList[rowcount - 1](item)
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
        # self.detresult.clear()
        ipgroupstr = self.netedit.text()
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
                    self.autofodun['sqlserver'][item] = ((item, tcpitem[1433]['product'], tcpitem[1433]['version']))
            if nm[item].has_tcp(1521):
                if tcpitem[1521]['state'] == 'open':
                    self.autofodun['oracle'][item] = ((item, tcpitem[1521]['product'], tcpitem[1521]['version']))

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

        if inputDlg.exec_() == QtWidgets.QDialog.Accepted:
            inputDlg.setDBIp(self.autofunList[self.detresult.currentIndex()][0])
            dbtype = self.autofunList[self.detresult.currentIndex()][1]
            dbtypeint = 0
            if dbtype == 'Mysql':
                dbtypeint = 3
            elif dbtype == 'Oracle':
                dbtypeint = 1
            elif dbtype == "MS SQL":
                dbtypeint = 2
            inputDlg.setDBtype(dbtypeint)
            inputDlg.setDBTypeVersion(self.autofunList[self.detresult.currentIndex()][2])
        QtWidgets.QMessageBox.warning(self, '版本限制', '现阶段并没有把自动发现的数据库添加的功能。')
        inputDlg.destroy()
