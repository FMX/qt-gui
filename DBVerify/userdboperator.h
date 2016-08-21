#ifndef USERDBOPERATOR_H
#define USERDBOPERATOR_H
#include "databaseinfoitem.h"
#include <QList>

class UserdbOperator
{
public:
    UserdbOperator();
    DatabaseInfoItem getOneByid();
    QList<DatabaseInfoItem> getAll();
    void saveOne(DatabaseInfoItem item);
    void saveAll(QList<DatabaseInfoItem> lst);
    void updateOneByid(int id, DatabaseInfoItem item);
};

#endif // USERDBOPERATOR_H
