# coding:utf-8
from PyQt5 import QtWidgets


class DBModifyDlg(QtWidgets.QDialog):
    def __init__(self, parent=None, index=-1, conn=None):
        super(DBModifyDlg, self).__init__()
        self.setWindowTitle(u"Modify DB Server Info")
        self.dbservelabel = QtWidgets.QLabel(u"DB Server Name")
        self.dbserveriplabel = QtWidgets.QLabel(u"DB Server IP")
        self.dbservertypelabel = QtWidgets.QLabel(u"DB Server Type")
        self.dbserverorassid = QtWidgets.QLabel(u"ORACLE SSID")
        self.dbserveruserlabel = QtWidgets.QLabel(u"DB Server User")
        self.dbserverpwdlabel = QtWidgets.QLabel(u"DB Server Password")
        self.dbserverostypelabel = QtWidgets.QLabel(u"OS Type")

        self.dbservertypeversionLabel = QtWidgets.QLabel(u"DB Version")
        self.dbserverostypeversionLabel = QtWidgets.QLabel(u"OS Version")
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

        self.btnAcp = QtWidgets.QPushButton(u"Confirm")
        self.btnCnl = QtWidgets.QPushButton(u"Cancel")

        self.dbserverportlabel = QtWidgets.QLabel(u"Port")
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

        # display
        if index != -1 and conn != None:
            item = conn.getOneDbitem(index)
            self.dbserveredit.setText(item.getDBName())
            self.dbserveripedit.setText(item.getDBip())
            self.dbservertypcmb.setCurrentIndex(item.getDBType())
            self.dbservertypeversionedit.setText(item.getDBVer())
            self.dbserverostypecmb.setCurrentIndex(item.getOsType())
            self.dbserverostypeversionedit.setText(item.getOsVersion())
            self.dbserverportedit.setText(str(item.getDBport()))
            self.dbserverorassidedit.setText(item.getOrasid())
            self.dbserveruseredit.setText(item.getDBUser())
            self.dbserverpwdedit.setText(item.getDBpwd())

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

    def getDBIP(self):
        return self.dbserveripedit.text()

    def getDBType(self):
        return self.dbservertypcmb.currentIndex() + 1

    def getDBTypeVersion(self):
        return self.dbservertypeversionedit.text()

    def getDBOsType(self):
        return self.dbserverostypecmb.currentIndex() + 1

    def getDBOsVersion(self):
        return self.dbserverostypeversionedit.text()

    def getDBport(self):
        return self.dbserverportedit.text()

    def getDBUsername(self):
        return self.dbserveruseredit.text()

    def getDBUserpwd(self):
        return self.dbserverpwdedit.text()

    def getDBOrasid(self):
        return self.dbserverorassidedit.text()
