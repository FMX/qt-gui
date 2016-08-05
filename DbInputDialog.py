# coding:utf-8
from PyQt5 import QtWidgets


class DBInputDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(DBInputDialog, self).__init__()
        self.setWindowTitle(u"添加数据库信息")
        self.dbservelabel = QtWidgets.QLabel(u"数据库服务器名称")
        self.dbserveriplabel = QtWidgets.QLabel(u"数据库IP地址")
        self.dbservertypelabel = QtWidgets.QLabel(u"数据库类型")
        self.dbserverorassid = QtWidgets.QLabel(u"ORACLE SSID")
        self.dbserveruserlabel = QtWidgets.QLabel(u"数据库用户名")
        self.dbserverpwdlabel = QtWidgets.QLabel(u"数据库用户名")
        self.dbserverostypelabel = QtWidgets.QLabel(u"操作系统类型")

        self.dbservertypeversionLabel = QtWidgets.QLabel(u"数据库版本")
        self.dbserverostypeversionLabel = QtWidgets.QLabel(u"操作系统版本")
        self.dbservertypeversionedit = QtWidgets.QLineEdit()
        self.dbserverostypeversionedit = QtWidgets.QLineEdit()

        self.dbserveredit = QtWidgets.QLineEdit()
        self.dbserveripedit = QtWidgets.QLineEdit()
        self.dbservertypcmb = QtWidgets.QComboBox()
        options = ["oracle", "sql server", "mysql"]
        self.dbservertypcmb.addItems(options)
        self.dbserverorassidedit = QtWidgets.QLineEdit()
        self.dbserveruseredit = QtWidgets.QLineEdit()
        self.dbserverpwdedit = QtWidgets.QLineEdit()

        self.dbserverostypecmb = QtWidgets.QComboBox()
        ostypes = ["windows", "linux", "unix"]
        self.dbserverostypecmb.addItems(ostypes)

        self.btnAcp = QtWidgets.QPushButton(u"确定")
        self.btnCnl = QtWidgets.QPushButton(u"取消")

        self.dbserverportlabel = QtWidgets.QLabel(u"端口")
        self.dbserverportedit = QtWidgets.QLineEdit()

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.dbservelabel, 1, 0)
        self.grid.addWidget(self.dbserveredit, 1, 1)
        self.grid.addWidget(self.dbserveriplabel, 2, 0)
        self.grid.addWidget(self.dbserveripedit, 2, 1)
        self.grid.addWidget(self.dbservertypelabel, 3, 0)
        self.grid.addWidget(self.dbservertypcmb, 3, 1)
        self.grid.addWidget(self.dbservertypeversionLabel, 4, 0)
        self.grid.addWidget(self.dbservertypeversionedit, 4, 1)
        self.grid.addWidget(self.dbserverorassid, 5, 0)
        self.grid.addWidget(self.dbserverorassidedit, 5, 1)
        self.grid.addWidget(self.dbserverostypelabel, 6, 0)
        self.grid.addWidget(self.dbserverostypecmb, 6, 1)
        self.grid.addWidget(self.dbserverostypeversionLabel, 7, 0)
        self.grid.addWidget(self.dbserverostypeversionedit, 7, 1)
        self.grid.addWidget(self.dbserverportlabel, 8, 0)
        self.grid.addWidget(self.dbserverportedit, 8, 1)
        self.grid.addWidget(self.dbserveruserlabel, 9, 0)
        self.grid.addWidget(self.dbserveruseredit, 9, 1)
        self.grid.addWidget(self.dbserverpwdlabel, 10, 0)
        self.grid.addWidget(self.dbserverpwdedit, 10, 1)

        self.grid.addWidget(self.btnAcp, 11, 1)
        self.grid.addWidget(self.btnCnl, 11, 0)

        self.setLayout(self.grid)
        self.setFixedSize(500, 650)
        # self.resize(500,400)

        self.btnAcp.clicked.connect(self.accept)
        # self.btnCnl.clicked.connect(self.cancel)
        self.btnCnl.clicked.connect(self.reject)

        self.dbservertypcmb.activated.connect(self.actcmb)

    def accept(self):
        QtWidgets.QDialog.accept(self)

    def reject(self):
        QtWidgets.QDialog.reject(self)

    def actcmb(self, index):
        print index
        if (index == 1 or index == 2):
            self.dbserverorassidedit.setEnabled(False)
            self.dbserverorassidedit.clear()
        if (index == 0):
            self.dbserverorassidedit.setEnabled(True)

    def getDataBaseDefines(self):
        return (self.dbserveredit.text(), self.dbserveripedit.text(),
                self.dbservertypcmb.currentIndex(), self.dbservertypeversionedit.text(),
                self.dbserverostypecmb.currentIndex(), self.dbserverostypeversionedit.text(),
                self.getDBport(), self.getDBOrasid(),
                self.getDBUsername(), self.getDBUserpwd())

    def getDBname(self):
        return self.dbserveredit.text()

    def setDBName(self, name):
        self.dbserveredit.setText(name)

    def getDBIP(self):
        return self.dbserveripedit.text()

    def setDBIp(self, ip):
        self.dbserveripedit.setText(ip)

    def getDBType(self):
        return self.dbservertypcmb.currentIndex() + 1

    def setDBtype(self, type):
        self.dbservertypcmb.setCurrentIndex(type)

    def getDBTypeVersion(self):
        return self.dbservertypeversionedit.text()

    def setDBTypeVersion(self, ver):
        self.dbservertypeversionedit.setText(ver)

    def getDBOsType(self):
        return self.dbserverostypecmb.currentIndex() + 1

    def setDBOsver(self, ver):
        self.dbserverostypecmb.setCurrentIndex(ver)

    def getDBOsVersion(self):
        return self.dbserverostypeversionedit.text()

    def setDBOsVer(self, ver):
        self.dbserverostypeversionedit.setText(ver)

    def getDBport(self):
        return self.dbserverportedit.text()

    def setDBPort(self, port):
        self.dbserverportedit.setText(port)

    def getDBUsername(self):
        return self.dbserveruseredit.text()

    def setDBUsername(self, usern):
        self.dbserveruseredit.setText(usern)

    def getDBUserpwd(self):
        return self.dbserverpwdedit.text()

    def setDBUserPwd(self, pwd):
        return self.dbserverpwdedit.setText(pwd)

    def getDBOrasid(self):
        return self.dbserverorassidedit.text()
