# coding:utf-8
import sqlite3

from DbItem import *


class DBConfigurations:
    __doc__ = '''Program Dao'''
    presetdbname = "./preset.db"
    userdbname = "./user.db"
    udb = None
    pdb = None

    newdbtarget_ful = "INSERT INTO dbs (dbname, dbip, dbtype, dbversion, ostype, osversion, dbport, orasid, username, userpwd)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

    updatedbtarget_ful = "update dbs set dbname=?,dbip=?,dbtype=?,dbversion=?,ostype=?,osversion=?,dbport=?,orasid=?,username=?,userpwd=? where id=?;"

    deletedbtarget = "delete from dbs where id=?"

    # loadAttackcode = "select Attcode from dbs where id=?"
    # loadVerifycode = "select Vercode from dbs where id=?"

    def __init__(self):
        self.connuser()
        self.connpre()
        self.precur = self.pdb.cursor()
        self.ucur = self.udb.cursor()

    def connuser(self):
        if self.udb == None:
            self.udb = sqlite3.connect(self.userdbname)

    def connpre(self):
        if self.pdb == None:
            self.pdb = sqlite3.connect(self.presetdbname)

    def addDB(self, dbname, dbip, dbtype, dbversion, ostype, osversion, dbport, orasid, username, userpwd):
        res = self.ucur.execute(self.newdbtarget_ful,
                                (dbname, dbip, dbtype, dbversion, ostype, osversion, dbport, orasid, username, userpwd))
        self.udb.commit()

    def updateDB(self, dbname, dbip, dbtype, dbversion, ostype, osversion, dbport, orasid, username, userpwd):
        res = self.ucur.execute(self.updatedbtarget_ful,
                                (dbname, dbip, dbtype, dbversion, ostype, osversion, dbport, orasid, username, userpwd))
        self.udb.commit()

    def getAttcode(self, leakindex):
        return self.precur.execute(self.loadAttackcode, (leakindex))

    def getVercode(self, leakindex):
        return self.precur.execute(self.loadVerifycode, (leakindex))

    def testDB(self):
        self.precur.execute("SELECT Attcode FROM leaks")

    def getUdbMaxIndex(self):
        self.ucur.execute("SELECT max(id) FROM dbs")
        data = self.ucur.fetchone()
        print data[0]
        return data[0]

    def getAllDbs(self):
        self.ucur.execute("SELECT * FROM dbs")
        return self.ucur.fetchall()

    def remoteDbitem(self, index):
        self.ucur.execute(self.deletedbtarget, (index))

    def getOneDbitem(self, index):
        self.ucur.execute("SELECT * FROM dbs")
        return DbItem(self.ucur.fetchone())

    def getDbServerInfos(self):
        self.ucur.execute("SELECT dbip,dbport FROM dbs;")
        return self.ucur.fetchall()

    def addNetDetBase(self, lst):
        self.ucur.execute("INSERT INTO dbs(dbname,dbip,dbtype,ostype,dbport) VALUES(?,?,?,?,?) ", lst)
        self.udb.commit()
