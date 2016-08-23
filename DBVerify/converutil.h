#ifndef CONVERUTIL_H
#define CONVERUTIL_H
#include <QString>

enum catagory{
    DB,OS
};

class ConverUtil
{
public:
    static QString TypeToString(int type,catagory cago);
    static int StringToType(QString str,int category);
};

#endif // CONVERUTIL_H
