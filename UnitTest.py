from DBConfigurations import DBConfigurations

if __name__ == "__main__":
    # print "DB Test"

    conf = DBConfigurations()
    # conf.addDB("test1","192.168.1.1",1,1,dbport=15, orasid="ORA10G", username="system", userpwd="yltest")
    # conf.getUdbMaxIndex()
    conf.getAllDbs()