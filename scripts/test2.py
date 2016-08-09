# coding:utf-8
from Base import Base


class test2(Base):
    def __init__(self):
        super(test2, self).__init__()

    def begin(self):
        Base.begin(self)
        print "TESE 2 "
