#ifndef DATABASEINFOITEM_H
#define DATABASEINFOITEM_H
#include <QString>

class DatabaseInfoItem
{
private:
    int id;
    QString dbname;
    QString dbip;
    int dbtype;
    QString dbversion;
    int dbport;
    QString orasid;
    QString username;
    QString userpwd;

    int fieldCnt=9;
public:
    DatabaseInfoItem();
};

#endif // DATABASEINFOITEM_H
