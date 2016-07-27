# coding:utf-8
import sqlite3


class DBConfigurations:
    presetdbname = "./preset.db"
    userdbname = "./user.db"
    db = None

    newdbtarget_min = "INSERT INTO dbs(dbname,dbip,dbtype,ostype) VALUES (?,?,?,?);"
    newdbtarget_ful = "insert INTO dbs(dbname,dbip,dbtype,ostype,dbport,orasid,username,userpwd) VALUES (?,?,?,?,?,?,?,?);"

    updatedbtarget_ful = "update dbs set dbname=?,dbip=?,dbtype=?,ostype=?,dbport=?,orasid=?,username=?,userpwd=? where id=?"

    deletedbtarget = "delete from dbs where id=?"

    loadAttackcode = "select Attcode from dbs where id=?"
    loadVerifycode = "select Vercode from dbs where id=?"

    def __init__(self):
        if self.db == None:
            db = sqlite3.connect(self.presetdbname)

    def addDB(self, dbname, dbip, dbtype, ostype):
        res = self.db.execute(self.newdbtarget_min, (dbname, dbip, dbtype, ostype))

    def addDB(self, dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd):
        res = self.db.execute(self.newdbtarget_ful, (dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd))

    def updateDB(self, dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd):
        res = self.db.execute(self.updatedbtarget_ful,
                              (dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd))

    def getAttcode(self, leakindex):
        return self.db.execute(self.loadAttackcode, (leakindex))

    def getVercode(self, leakindex):
        return self.db.execute(self.loadVerifycode, (leakindex))

    def testDB(self):
        self.db.execute(".header on")
        self.db.execute("select Attcode from dbs")
