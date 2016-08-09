# coding:utf-8

class DbItem:
    def __init__(self, lst):
        self.dbn = lst[1]
        self.dbi = lst[2]
        self.dbt = lst[3]
        self.dbtv = lst[4]
        self.ot = lst[5]
        self.ov = lst[6]
        self.dp = lst[7]
        self.ra = lst[8]
        self.un = lst[9]
        self.pw = lst[10]

    def getDBItemInfo(self):
        return (self.dbn, self.dbi, self.dbt, self.dbtv, self.ot, self.ov, self.dp, self.ra, self.un, self.pw)

    def getDBName(self):
        return self.dbn

    def getDBip(self):
        return self.dbi

    def getDBType(self):
        return self.dbt - 1

    def getDBVer(self):
        return self.dbtv

    def getOsType(self):
        return self.ot + 1

    def getOsVersion(self):
        return self.ov

    def getDBport(self):
        return self.dp

    def getOrasid(self):
        return self.ra

    def getDBUser(self):
        return self.un

    def getDBpwd(self):
        return self.pw
