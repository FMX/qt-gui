# coding:utf-8
from   sqlobject import *
class DBS(SQLObject):
    dbname=StringCol()
    dbip=StringCol()
    dbtype=IntCol()
    ostype=IntCol()
    dbport=IntCol()
    orasid=StringCol()
    username=StringCol()
    userpwd=StringCol()