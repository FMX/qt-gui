# coding:utf-8
import sqlite3
from sqlobject.sqlite import builder

class DBConfigurations:
    presetdbname = "./preset.db"
    userdbname = "./user.db"
    udb = None
    pdb = None

    newdbtarget_min = "INSERT INTO dbs(dbname,dbip,dbtype,ostype) VALUES (?,?,?,?);"
    newdbtarget_ful = "insert INTO dbs(dbname,dbip,dbtype,ostype,dbport,orasid,username,userpwd) VALUES (?,?,?,?,?,?,?,?);"

    updatedbtarget_ful = "update dbs set dbname=?,dbip=?,dbtype=?,ostype=?,dbport=?,orasid=?,username=?,userpwd=? where id=?"

    deletedbtarget = "delete from dbs where id=?"

    loadAttackcode = "select Attcode from dbs where id=?"
    loadVerifycode = "select Vercode from dbs where id=?"

    def connuser(self):
        if self.udb == None:
            self.udb = sqlite3.connect(self.userdbname)

    def connpre(self):
        if self.pdb == None:
            self.pdb = sqlite3.connect(self.presetdbname)

    def addDB(self, dbname, dbip, dbtype, ostype):
        res = self.udb.execute(self.newdbtarget_min, (dbname, dbip, dbtype, ostype))

    def addDB(self, dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd):
        res = self.udb.execute(self.newdbtarget_ful, (dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd))

    def updateDB(self, dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd):
        res = self.udb.execute(self.updatedbtarget_ful,
                               (dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd))

    def getAttcode(self, leakindex):
        return self.pdb.execute(self.loadAttackcode, (leakindex))

    def getVercode(self, leakindex):
        return self.pdb.execute(self.loadVerifycode, (leakindex))

    def testDB(self):
        self.pdb.execute(".header on")
        self.pdb.execute("select Attcode from leaks")

