# coding:utf-8
import sqlite3


class DBConfigurations:
    dbname = "./dbconf.sqlite3"
    db = None

    def __init__(self):
        if self.db == None:
            db = sqlite3.connect(self.dbname)
            db.execute("CREATE TABLE dbs(id INT PRIMARY KEY NOT NULL ,"
                       "Dbname TEXT NOT NULL ,"
                       "Dbip TEXT NOT NULL ,"
                       "Dbtype INT NOT NULL ,"
                       "Orasid TEXT ,"
                       "Username TEXT ,"
                       "Userpwd TEXT)")

            db.execute("CREATE TABLE leaks(id INT PRIMARY KEY NOT NULL ,"
                       "Leakname TEXT NOT NULL ,"
                       "Dbtype INT NOT NULL ,"
                       "Dbversion TEXT NOT NULL ,"
                       "OsType INT NOT NULL ,"
                       "OsVersion TEXT NOT NULL ,"
                       "Code TEXT NOT NULL )")

    def addDB(self, name, type, ip, username, pwd):
        print "Add a target database"
