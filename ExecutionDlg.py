# coding:utf-8
from PyQt5 import QtCore, QtWidgets


class ExecutionDlg(QtWidgets.QDialog):
    def __init__(self, parent=None, dbindex=0, leakindex=0):
        super(ExecutionDlg, self).__init__()
        self.setWindowTitle(u"验证")
        self.resize(550, 600)

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

    def accept(self):
        QtWidgets.QDialog.accept(self)
