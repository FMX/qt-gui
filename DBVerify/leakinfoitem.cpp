#include "leakinfoitem.h"

LeakinfoItem::LeakinfoItem()
{

}

LeakinfoItem::LeakinfoItem(QString leakname,int dbtypes,QString dbtype,int ostypecnt,QString osversion,int reqpwd)
{
    this->leakname=leakname;
    this->dbtypes=dbtypes;
    this->dbtype=dbtype;
    this->ostypeCnt=ostypecnt;
    this->osversion=osversion;
    this->reqpwd=reqpwd;
}

LeakinfoItem::LeakinfoItem(QString leakname,QString cvename,QString leakdesc,int dbtypes,QString dbtype,
                           QString dbversion,int ostypecnt,QString ostype,QString osversino,int reqpwd,QString modulename)
{
    this->leakname=leakname;
    this->cvename=cvename;
    this->leakdesc=leakdesc;
    this->dbtypes=dbtypes;
    this->dbversion=dbversion;
    this->ostypeCnt=ostypecnt;
    this->ostype=ostype;
    this->osversion=osversino;
    this->reqpwd=reqpwd;
    this->modulename=modulename;
}

int LeakinfoItem::getId()
{
    return this->id;
}

QString LeakinfoItem::getLeakname()
{
    return this->leakname;
}

QString LeakinfoItem::getCvename()
{
    return this->cvename;
}

int LeakinfoItem::getDbtypes()
{
    return this->dbtypes;
}

QString LeakinfoItem::getDbtype()
{
    QString typeBuf;
    QStringList lst= this->dbtype.split(",");

    QStringList::const_iterator it;
    for(it=lst.constBegin();it!=lst.constEnd();++it)
    {
        int type=(*it).toInt();
        switch (type) {
        case 0:
            typeBuf.append("ORACLE ");
            break;
        case 1:
            typeBuf.append("MYSQL ");
            break;
        case 2:
            typeBuf.append("SQL SERVER ");
            break;
        default:
            break;
        }
    }

    return typeBuf;
}

QString LeakinfoItem::getDbversion()
{
    return this->dbversion;
}

int LeakinfoItem::getOstypecnt()
{
    return this->ostypeCnt;
}

QString LeakinfoItem::getOstype()
{

    QString typeBuf;
    QStringList lst= this->ostype.split(",");

    QStringList::const_iterator it;
    for(it=lst.constBegin();it!=lst.constEnd();++it)
    {
        int type=(*it).toInt();
        switch (type) {
        case 0:
            typeBuf.append("Windows ");
            break;
        case 1:
            typeBuf.append("Linux ");
            break;
        case 2:
            typeBuf.append("Unix ");
            break;
        default:
            break;
        }
    }

    return typeBuf;
}

QString LeakinfoItem::getOsversion()
{
    return this->osversion;
}

int LeakinfoItem::getReqpwd()
{
    return this->reqpwd;
}

QString LeakinfoItem::getModulename()
{
    return this->modulename;
}

void LeakinfoItem::setLeakname(QString dbname)
{

}

void LeakinfoItem::setCvename(QString cvename)
{

}

void LeakinfoItem::setDbtypes(int types)
{

}

void LeakinfoItem::setDbtype(QString type)
{

}

void LeakinfoItem::setDbversion(QString version)
{

}

void LeakinfoItem::setOstypecnt(int cnt)
{

}

void LeakinfoItem::setOstype(QString ostype)
{

}

void LeakinfoItem::setOsversion(QString version)
{

}

void LeakinfoItem::setReqpwd(int req)
{

}

void LeakinfoItem::setModulename(QString name)
{

}

void LeakinfoItem::setId(int id)
{
    this->id=id;
}


QString LeakinfoItem::getLeakdesc()
{
    return this->leakdesc;
}

void LeakinfoItem::setLeakDesc(QString desc)
{
    this->leakdesc=desc;
}

