#ifndef LEAKINFOITEM_H
#define LEAKINFOITEM_H
#include <QString>

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

    int fieldCnt=12;
public:
    LeakinfoItem();
};

#endif // LEAKINFOITEM_H
