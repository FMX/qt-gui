# coding:utf-8
from sqlobject import *
import os
import dbs

class UserDB:
    connection=None

    def __init__(self):
        if self.connection == None:
            db_filename = os.path.abspath('udb.db')
            if os.path.exists(db_filename):
                os.unlink(db_filename)
                connection_string = 'sqlite:' + db_filename
                self.connection = connectionForURI(connection_string)
                sqlhub.processConnection = self.connection

    def getList(self):
        return dbs.select()

    def newDb(self,dbname, dbip, dbtype, ostype, dbport, orasid, username, userpwd):
        dbs(dbname=dbname,dbip=dbip,dbtype=dbtype,ostype=ostype,dbport=dbport,orasid=orasid,username=username,userpwd=userpwd)

