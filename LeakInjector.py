# coding:utf-8
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys


class LeakInjector(QtWidgets.QMainWindow):
    def __init__(self):
        super(LeakInjector, self).__init__()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = LeakInjector()
    ui.show()
    app.exec_()
