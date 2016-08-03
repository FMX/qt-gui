# coding:utf-8
import nmap
from PyQt5 import QtCore, QtWidgets


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
        self.detresult.setColumnCount(3)
        self.detresult.setHorizontalHeaderLabels([u"IP", u"数据库", u"操作系统"])
        self.verticalLayout.addLayout(self.horizontalLayout_2)

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
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.horizontalLayout_3.addWidget(self.btnconfirm)
        self.btncancel = QtWidgets.QPushButton(u"取消")
        self.horizontalLayout_3.addWidget(self.btncancel)
        self.btncancel.setStyleSheet(
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btncancel.clicked.connect(self.reject)
        self.btnconfirm.clicked.connect(self.accept)

        self.btnDet.clicked.connect(self.detectNewWork)

        self.autofodun = {}
        # self.sqlserdet = {}
        # self.oracledet = {}

        # thread=NmapThread()
        # thread._signal.connect(self.testSlot)
        # thread.start()

    def displayScanres(self):
        self.detresult.clear()
        print self.mysqldet
        print self.sqlserdet
        print self.oracledet

    def accept(self):
        QtWidgets.QDialog.accept(self)
        print "accept"

    def reject(self):
        QtWidgets.QDialog.reject(self)
        print "reject"

    def detectNewWork(self):
        print "Detect"
        ipgroupstr = self.netedit.text()
        lst = ipgroupstr.split(".")
        print lst[0], lst[1], lst[2]
        nm = nmap.PortScanner()
        hoststring = '%s.%s.%s.1/24' % (lst[0], lst[1], lst[2])
        print hoststring
        self.progress.setValue(15)
        # for ip in range(2, 255):
        nm.scan(hosts="192.168.30.113/24", ports="1433,3306,1433")
        # self.scanresult.append(nm.all_hosts())
        # self.progress.setValue(int(ip / 255))
        # while nm.still_scanning():
        #     nm.wait(5)
        hosts = nm.all_hosts()

        # print nm[hosts][3306]
        # print hosts
        for item in hosts:
            tcpitem = nm[item]['tcp']
            print tcpitem
            if nm[item].has_tcp(3306):
                # print tcpitem[3306]
                if tcpitem[3306]['state'] == 'open':
                    self.mysqldet[item] = (tcpitem[3306]['product'], tcpitem[3306]['version'])
            if nm[item].has_tcp(1433):
                if tcpitem[1433]['state'] == 'open':
                    self.sqlserdet[item] = (tcpitem[3306]['product'], tcpitem[3306]['version'])
                    # print tcpitem[1433]
            if nm[item].has_tcp(1521):
                if tcpitem[1521]['state'] == 'open':
                    self.oracledet[item] = (tcpitem[3306]['product'], tcpitem[3306]['version'])
                    # print tcpitem[1521]

        print ""
        print ""
        self.finishDet()
        self.displayScanres()

    def finishDet(self):
        self.progress.setValue(100)

    def nmapcallback(self, host, res):
        self.scanresult.append(res)
        print host
        print res
