# coding:utf-8
import sys
from PyQt5 import QtGui, QtCore, QtWidgets


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

        self.dbserveredit = QtWidgets.QLineEdit()
        self.dbserveripedit = QtWidgets.QLineEdit()
        self.dbservertypcmb = QtWidgets.QComboBox()
        options = ["oracle", "sql server", "mysql"]
        self.dbservertypcmb.addItems(options)
        self.dbserverorassidedit = QtWidgets.QLineEdit()
        self.dbserveruseredit = QtWidgets.QLineEdit()
        self.dbserverpwdedit = QtWidgets.QLineEdit()

        self.btnAcp = QtWidgets.QPushButton(u"确定")
        self.btnCnl = QtWidgets.QPushButton(u"取消")

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.dbservelabel, 1, 0)
        self.grid.addWidget(self.dbserveredit, 1, 1)
        self.grid.addWidget(self.dbserveriplabel, 2, 0)
        self.grid.addWidget(self.dbserveripedit, 2, 1)
        self.grid.addWidget(self.dbservertypelabel, 3, 0)
        self.grid.addWidget(self.dbservertypcmb, 3, 1)
        self.grid.addWidget(self.dbserverorassid, 4, 0)
        self.grid.addWidget(self.dbserverorassidedit, 4, 1)
        self.grid.addWidget(self.dbserveruserlabel, 5, 0)
        self.grid.addWidget(self.dbserveruseredit, 5, 1)
        self.grid.addWidget(self.dbserverpwdlabel, 6, 0)
        self.grid.addWidget(self.dbserverpwdedit, 6, 1)

        self.grid.addWidget(self.btnAcp, 7, 1)
        self.grid.addWidget(self.btnCnl, 7, 0)

        self.setLayout(self.grid)
        self.setFixedSize(500, 500)
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
