# coding:utf-8
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
        self.scriptused = lst[11]
        self.script1 = lst[12]
        self.script2 = lst[13]
        self.script3 = lst[14]
        self.script4 = lst[15]
        self.script5 = lst[16]
        self.script6 = lst[17]
        self.script7 = lst[18]
        self.script8 = lst[19]
        self.username = lst[20]
        self.userpwd = lst[21]

    def getid(self):
        return self.id

    def getLeakName(self):
        return self.leakname

    def getCvename(self):
        return self.cvename

    def getdbtypes(self):
        return self.dbtypes

    def getdbtype(self):
        return self.dbtype

    def getDBVersion(self):
        return self.dbversion

    def getOsTypeCnt(self):
        return self.ostypeCnt

    def getOsType(self):
        return self.ostype

    def getOsVer(self):
        return self.osver

    def getReqpwd(self):
        return self.reqpwd

    def getScriptused(self):
        return self.scriptused

    def getScript1(self):
        return self.script1

    def getScript2(self):
        return self.script2

    def getScript3(self):
        return self.script3

    def getScript4(self):
        return self.script4

    def getScript5(self):
        return self.script5

    def getScript6(self):
        return self.script6

    def getScript7(self):
        return self.script7

    def getScript8(self):
        return self.script8

    def getUsername(self):
        return self.username

    def getUserpwd(self):
        return self.userpwd
