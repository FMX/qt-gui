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
    int ostype;
    QString osversion;
    int dbport;
    QString orasid;
    QString username;
    QString userpwd;

public:
    DatabaseInfoItem();
    DatabaseInfoItem(QString dbname,QString dbip,int dbtype,int dbport);
    DatabaseInfoItem(QString dbname,QString dbip,int dbtype,QString dbversion,int ostype,QString osversion,int dbport,QString orasid,QString username,QString usepwd);

    int getId();
    QString getDbname();
    QString getDbip();
    int getDbtype();
    QString getDbversion();
    int getOstype();
    QString getOsversion();
    int getDbport();
    QString getOrasid();
    QString getUsername();
    QString getUserpwd();

    void setDbname(QString name);
    void setDbip(QString ip);
    void setDbtype(int type);
    void setDbversion(QString version);
    void setOstype(int type);
    void setOsversion(QString version);
    void setDbport(int port);
    void setOrasid(QString orasid);
    void setUsername(QString name);
    void setUserpwd(QString pwd);

};

#endif // DATABASEINFOITEM_H
