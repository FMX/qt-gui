# coding:utf-8
from TypeParser import *


class LeakItem:
    def __init__(self, lst):
        self.id = lst[0]
        self.leakname = lst[1]
        self.cvename = lst[2]
        self.leakdesc = lst[3]
        self.dbtypes = lst[4]
        self.dbtype = lst[5]
        self.dbversion = lst[6]
        self.ostypeCnt = lst[7]
        self.ostype = lst[8]
        self.osver = lst[9]
        self.reqpwd = lst[10]
        self.scriptname = lst[11]

    def getid(self):
        return self.id

    def getLeakName(self):
        return self.leakname

    def getCvename(self):
        return self.cvename

    def getdbtypes(self):
        return self.dbtypes

    def getdbtype(self):
        type = TypeParse()
        if self.getdbtypes() > 1:
            str = ""
            for item in self.dbtype.split(","):
                str = str + type.parDBType(int(item)) + " "
            return str
        elif self.getdbtypes() == 1:
            return type.parDBType(self.dbtype)

    def getDBVersion(self):
        return self.dbversion

    def getOsTypeCnt(self):
        return self.ostypeCnt

    def getOsType(self):
        return self.ostype

    def getOsVer(self):
        return self.osver

    def getReqpwd(self):
        if self.reqpwd == 1:
            return u"Necessary"
        else:
            return u"UnNecessary"
    
    def getScriptName(self):
        return self.scriptname
