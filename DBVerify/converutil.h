#ifndef CONVERUTIL_H
#define CONVERUTIL_H
#include <QString>
#include <QStringList>
#include <QRegExp>

enum catagory{
    DB,OS
};

struct TypeAndCnt{
    int type;
    QString typeStr;
};

class ConverUtil
{
public:
    static QString TypeToString(int type);
    static QString OsTypeToString(int type);
    static QString TypeToString(int typecnt,QString type);
    static QString OsTypeToString(int oscnt,QString type);
    static QString ReqpwdToString(int req);
    static int StringToType(QString str,catagory type);
};

#endif // CONVERUTIL_H
