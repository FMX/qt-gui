#ifndef USERDBOPERATOR_H
#define USERDBOPERATOR_H
#include "databaseinfoitem.h"
#include <QList>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QMessageBox>
#include <QVariant>
#include <QSqlError>
#include <QDebug>

class UserdbOperator
{
private:
    QSqlDatabase database;
public:
    UserdbOperator();
    DatabaseInfoItem getOneByid(int id);
    QList<DatabaseInfoItem> getAll();
    void saveOne(DatabaseInfoItem item);
    void saveAll(QList<DatabaseInfoItem> lst);
    void updateOneByid(int id, DatabaseInfoItem item);
};

#endif // USERDBOPERATOR_H
