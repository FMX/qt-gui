#include "converutil.h"


QString ConverUtil::TypeToString(int type,catagory cago)
{
    QString buf;
    if(cago==catagory::DB) //db
    {
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
    }
    if(cago==catagory::OS) //os
    {
        switch (type) {
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
            break;
        }
    }

    return buf;
}

int ConverUtil::StringToType(QString str,int category)
{

}
