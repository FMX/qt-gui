#ifndef DATABASEOPERATOR_H
#define DATABASEOPERATOR_H
#include <QString>
#include <QDebug>
#include <QSqlDatabase>
#include <QSqlQuery>

#include "databaseinfoitem.h"
#include "leakinfoitem.h"
#include <QVector>
#include <QList>

class DataBaseOperator
{
private:
    QString fname=nullptr;
public:
    DataBaseOperator(QString filename);

    //databaseinfo relative
    DatabaseInfoItem getDatabaseInfoById(int id);
    QList<DatabaseInfoItem> getDatabaseInfos();

    //leakinfo relative
    LeakinfoItem getLeakinfoItemById(int id);
    QList<LeakinfoItem> getLeakInfoItems();

};

#endif // DATABASEOPERATOR_H
