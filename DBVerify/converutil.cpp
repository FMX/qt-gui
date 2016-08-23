#include "converutil.h"


QString ConverUtil::TypeToString(int type)
{
    QString buf;

    switch (type) {
    case 1:
        buf="Oracle";
        break;
    case 2:
        buf="Sql Server";
        break;
    case 3:
        buf="Mysql";
        break;
    default:
        break;
    }

    return buf;
}

QString ConverUtil::TypeToString(int typecnt,QString type)
{
    QStringList lst=type.split(",");
    if(lst.size()!=typecnt)
        return "Unknown!";
    QString str;
    foreach (QString buf, lst)
    {
        str.append(ConverUtil::TypeToString(buf.toInt()));
        str.append(";");
    }
    QString pattern=";$";
    QRegExp reg(pattern);
    str.remove(reg);
    return str;
}

QString ConverUtil::OsTypeToString(int oscnt,QString type)
{
    QStringList lst=type.split(",");
    if(lst.size()!=oscnt)
        return "Unknown";
    QString str;
    foreach(QString buf,lst)
    {
        str.append(ConverUtil::OsTypeToString(buf.toInt()));
        str.append(";");
    }
    QString pattern=";$";
    QRegExp reg(pattern);
    str.remove(reg);
    return str;
}

QString ConverUtil::OsTypeToString(int type)
{
    QString buf;
    switch(type)
    {
    case 1:
        buf="Windows";
        break;
    case 2:
        buf="Linux";
        break;
    case 3:
        buf="Unix";
        break;
    default:
        buf="Unknown";
        break;
    }
    return buf;
}

QString ConverUtil::ReqpwdToString(int req)
{
    if(req==0)
        return "不需要";
    if(req==1)
        return "需要";
}

static int StringToType(QString str,catagory type)
{

}
