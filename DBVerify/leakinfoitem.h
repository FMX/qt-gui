#ifndef LEAKINFOITEM_H
#define LEAKINFOITEM_H
#include <QString>
#include <QStringList>

class LeakinfoItem
{
private:
    int id;
    QString leakname;
    QString cvename;
    QString leakdesc;
    int dbtypes;
    QString dbtype;
    QString dbversion;
    int ostypeCnt;
    QString ostype;
    QString osversion;
    int reqpwd;
    QString modulename;

public:
    LeakinfoItem();
    LeakinfoItem(QString leakname,int dbtypes,QString dbtype,int ostypecnt,QString osversion,int reqpwd);
    LeakinfoItem(QString leakname,QString cvename,QString leakdesc,int dbtypes,QString dbtype,QString dbversion,int ostypecnt,QString ostype,QString osversino,int reqpwd,QString modulename);

    int getId();
    QString getLeakname();
    QString getCvename();
    int getDbtypes();
    QString getDbtype();
    QString getDbversion();
    int getOstypecnt();
    QString getOstype();
    QString getOsversion();
    int getReqpwd();
    QString getModulename();

    void setLeakname(QString dbname);
    void setCvename(QString cvename);
    void setDbtypes(int types);
    void setDbtype(QString type);
    void setDbversion(QString version);
    void setOstypecnt(int cnt);
    void setOstype(QString ostype);
    void setOsversion(QString version);
    void setReqpwd(int req);
    void setModulename(QString name);

};

#endif // LEAKINFOITEM_H
