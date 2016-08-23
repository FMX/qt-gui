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
    this->dbname=name;
}

void DatabaseInfoItem::setDbip(QString ip)
{
    this->dbip=ip;
}

void DatabaseInfoItem::setDbtype(int type)
{
    this->dbtype=type;
}

void DatabaseInfoItem::setDbversion(QString version)
{
    this->dbversion=version;
}

void DatabaseInfoItem::setOstype(int type)
{
    this->ostype=type;
}

void DatabaseInfoItem::setOsversion(QString version)
{
    this->osversion=version;
}

void DatabaseInfoItem::setDbport(int port)
{
    this->dbport=port;
}

void DatabaseInfoItem::setOrasid(QString orasid)
{
    this->orasid=orasid;
}

void DatabaseInfoItem::setUsername(QString name)
{
    this->username=name;
}

void DatabaseInfoItem::setUserpwd(QString pwd)
{
    this->userpwd=pwd;
}

void DatabaseInfoItem::setId(int id)
{
    this->id=id;
}
