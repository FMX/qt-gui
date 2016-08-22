#include "databaseinfoitem.h"

DatabaseInfoItem::DatabaseInfoItem()
{

}

DatabaseInfoItem::DatabaseInfoItem(QString dbname,QString dbip,int dbtype,int dbport)
{
    this->dbname=dbname;
    this->dbip=dbip;
    this->dbtype=dbtype;
    this->dbport=dbport;
}

DatabaseInfoItem::DatabaseInfoItem(QString dbname,QString dbip,int dbtype,QString dbversion,
                                   int ostype,QString osversion,int dbport,QString orasid,QString username,QString usepwd)
{
    this->dbname=dbname;
    this->dbip=dbip;
    this->dbtype=dbtype;
    this->dbversion=dbversion;
    this->ostype=ostype;
    this->osversion=osversion;
    this->dbport=dbport;
    this->orasid=orasid;
    this->username=username;
    this->userpwd=usepwd;
}

int DatabaseInfoItem::getId()
{
    return this->id;
}

QString DatabaseInfoItem::getDbname()
{
    return this->dbname;
}

QString DatabaseInfoItem::getDbip()
{
    return this->dbip;
}

int DatabaseInfoItem::getDbtype()
{
//    switch (this->dbtype) {
//    case 0:
//       return QString("ORACLE");
//    case 1:
//        return QString("MYSQL");
//    case 2:
//        return QString("SQL SERVER");
//    default:
//        return QString("Unknown");
//    }
    return this->dbtype;
}

QString DatabaseInfoItem::getDbversion()
{
    return this->dbversion;
}

int DatabaseInfoItem::getOstype()
{
//    switch (this->ostype) {
//    case 1:
//        return QString("Windows");
//    case 2:
//        return QString("Linux");
//    case 3:
//        return QString("Unix");
//    default:
//        return QString("Unknown");
//    }
    return this->ostype;
}

QString DatabaseInfoItem::getOsversion()
{
    return this->osversion;
}

int DatabaseInfoItem::getDbport()
{
    return this->dbport;
}

QString DatabaseInfoItem::getOrasid()
{
    return this->orasid;
}

QString DatabaseInfoItem::getUsername()
{
    return this->username;
}

QString DatabaseInfoItem::getUserpwd()
{
    return this->userpwd;
}

void DatabaseInfoItem::setDbname(QString name)
{

}

void DatabaseInfoItem::setDbip(QString ip)
{

}

void DatabaseInfoItem::setDbtype(int type)
{

}

void DatabaseInfoItem::setDbversion(QString version)
{

}

void DatabaseInfoItem::setOstype(int type)
{

}

void DatabaseInfoItem::setOsversion(QString version)
{

}

void DatabaseInfoItem::setDbport(int port)
{

}

void DatabaseInfoItem::setOrasid(QString orasid)
{

}

void DatabaseInfoItem::setUsername(QString name)
{

}

void DatabaseInfoItem::setUserpwd(QString pwd)
{

}

void DatabaseInfoItem::setId(int id)
{
    this->id=id;
}
