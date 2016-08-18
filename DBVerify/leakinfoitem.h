#ifndef LEAKINFOITEM_H
#define LEAKINFOITEM_H


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
};

#endif // LEAKINFOITEM_H
