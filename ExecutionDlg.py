# coding:utf-8
import StringIO
import importlib
import sys

from PyQt5 import QtCore, QtWidgets

from DBConfigurations import *


class ExecutionDlg(QtWidgets.QDialog):
    def __init__(self, parent=None, dbid=0, leakid=0):
        super(ExecutionDlg, self).__init__()
        self.setWindowTitle(u"验证")
        self.resize(550, 600)

        self.dbConn = DBConfigurations()

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 550, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.resultarea = QtWidgets.QTextEdit()
        self.horizontalLayout.addWidget(self.resultarea)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setSpacing(6)
        self.horizontalLayout1.setContentsMargins(11, 11, 11, 11)
        self.btncfm = QtWidgets.QPushButton(u"关闭")
        self.horizontalLayout1.addWidget(self.btncfm)
        self.btncfm.setStyleSheet(
            '''color:blue;background-color: yellow;selection-background-color: blue;border:2px groove gray;border-radius:10px;padding:2px 4px''')
        self.verticalLayout.addLayout(self.horizontalLayout1)

        self.btncfm.clicked.connect(self.close)

        self.dbid = dbid
        self.leakid = leakid

        self.dbConnection = DBConfigurations()

        self.loadDbInfo()
        self.loadLeakInfo()
        if self.checkDep():
            self.runscript()
        else:
            self.resultarea.setText(u"漏洞和数据库信息不匹配")

    def loadDbInfo(self):
        self.dbitem = self.dbConnection.getOneDbitem(self.dbid)

    def loadLeakInfo(self):
        self.leakitem = self.dbConnection.getOneLeakItem(self.leakid)

    def checkDep(self):
        return True

    def runscript(self):
        codeOut = StringIO.StringIO()
        codeErr = StringIO.StringIO()
        scriptname = self.leakitem.getScriptName()

        tmp = sys.stdout
        tmp1 = sys.stderr

        sys.stdout = codeOut
        sys.stderr = codeErr

        mod = importlib.import_module("scripts")
        submode = getattr(mod, self.leakitem.getScriptName())
        classobj = getattr(submode, self.leakitem.getScriptName())
        obj = classobj()
        obj.begin()

        self.resultarea.setText(codeOut.getvalue())
        sys.stdout = tmp
        sys.stderr = tmp1

    def accept(self):
        QtWidgets.QDialog.accept(self)
