# coding:utf-8

import mysql.connector


class mysql_pri1:
    def __init__(self):
        pass

    def setDBInfo(self, dbinfo):
        self.dbip = dbinfo[1]
        self.dbname = dbinfo[8]
        self.dbpwd = dbinfo[9]

    def pro(self):
        self.connToDB()

    def connToDB(self):
        config = {'host': self.dbip, 'user': self.dbname, 'password': self.dbpwd, 'port': 3306}
        try:
            self.mysql = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print "Connect to DB Failed!Failure is {}".format(e)
            print "Attack Failed!"
            return

