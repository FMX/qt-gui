# coding:utf-8


class TypeParse:
    def __init__(self):
        self.dbtype = {1: 'oracle', 2: 'sql server', 3: 'mysql'}
        self.ostype = {1: 'windows', 2: 'linux', 3: 'unix'}

    def parDBType(self, dbtype):
        return self.dbtype.get(dbtype)

    def parOSType(self, ostype):
        return self.ostype.get(ostype)
